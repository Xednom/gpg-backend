import datetime
import calendar

from decimal import Decimal

from django.db.models import Sum, Q, F
from django.core.management.base import BaseCommand

from apps.authentication.models import Staff
from apps.timesheet.models import (
    AccountCharge,
    StaffPaymentHistory,
    StaffAccountBalance,
)


class Command(BaseCommand):
    help = "Automatically create Staff Account balance for every user in the system monthly(1st, 15th and 16th 30th-31st)."

    def handle(self, *args, **kwargs):
        staff_name = (
            AccountCharge.objects.filter(status="approved")
            .values_list("staff", flat=True)
            .distinct()
        )
        today = datetime.date.today()
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month
        current_date = calendar.monthrange(current_year, current_month)[1]
        staff = Staff.objects.filter(id__in=staff_name)
        staff_timesheet = Staff.objects.filter(
            id__in=staff_name, user__is_active=True
        ).exists()
        current_time = datetime.date.today()
        current_day = datetime.date.today().day
        every_1st = datetime.date.today().replace(day=1)
        every_15th = datetime.date.today().replace(day=15)
        every_16th = datetime.date.today().replace(day=16)
        every_31st = datetime.date.today().replace(day=current_date)
        every_30th = datetime.date.today().replace(day=current_date)
        day_1st_and_15th = str(every_1st) + " " + str(every_15th)
        day_16th_and_30th = str(every_16th) + " " + str(every_30th)
        day_16th_and_31st = str(every_16th) + " " + str(every_31st)
        print(current_day)
        print(current_date)

        for i in staff:
            if staff_timesheet:
                staff_charge = AccountCharge.objects.filter(staff=i).exists()
                staff_balance = StaffAccountBalance.objects.filter(staff=i).exists()
                staff_name = AccountCharge.objects.filter(staff=staff_charge)
                staff_balance_first_half_month = StaffAccountBalance.objects.filter(
                    staff=i, date=day_1st_and_15th
                ).exists()
                staff_balance_second_half_month = StaffAccountBalance.objects.filter(
                    staff=i, date=day_16th_and_30th
                ).exists()
                staff_balance_second_half_month_with_31 = (
                    StaffAccountBalance.objects.filter(
                        staff=i, date=day_16th_and_31st
                    ).exists()
                )
            staff_time_charge_1st_and_15th = AccountCharge.objects.filter(
                staff=i, shift_date__gte=every_1st, shift_date__lte=every_15th
            ).aggregate(totals=Sum("total_time"), total_charge=Sum("staff_total_due"))
            staff_time_charge_16th_and_30th = AccountCharge.objects.filter(
                staff=i, shift_date__gte=every_16th, shift_date__lte=every_30th
            ).aggregate(totals=Sum("total_time"), total_charge=Sum("staff_total_due"))
            staff_time_charge_16th_and_31st = AccountCharge.objects.filter(
                staff=i, shift_date__gte=every_16th, shift_date__lte=every_31st
            ).aggregate(totals=Sum("total_time"), total_charge=Sum("staff_total_due"))
            staff_payment_1st_and_15th = StaffPaymentHistory.objects.filter(
                staff=i, date__range=[every_1st, every_15th]
            ).aggregate(total_payment=Sum("amount"))
            staff_payment_16th_and_31st = StaffPaymentHistory.objects.filter(
                staff=i, date__range=[every_16th, every_31st]
            ).aggregate(total_payment=Sum("amount"))
            staff_payment_16th_and_30th = StaffPaymentHistory.objects.filter(
                staff=i, date__range=[every_16th, every_30th]
            ).aggregate(total_payment=Sum("amount"))

            staff_payment = StaffPaymentHistory.objects.filter(staff=i).aggregate(
                total_payment=Sum("amount")
            )
            # staff_charge = AccountCharge.objects.filter(staff=i).aggregate(
            #     total_charge=Sum("staff_total_due")
            # )

            # if staff_time_charge_1st_and_15th["total_charge"] is not None:
            #     print("Total charge: ", staff_time_charge_1st_and_15th["total_charge"])

            # if staff_payment_1st_and_15th["total_payment"] is not None:
            #     print("Total amount: ", staff_payment_1st_and_15th["total_payment"])

            # StaffAccountBalance.objects.all().delete()
            # for name in staff_name:
            #     print(name.staff)

            # print(day_16th_and_31st)

            # if staff_charge:
            #     if (
            #         staff_payment["total_payment"] is None
            #         and staff_charge["total_charge"] is None
            #     ):
            #         StaffAccountBalance.objects.create(
            #             date=today,
            #             staff=i,
            #             payment_made=0.00,
            #             amount_due=0.00,
            #             account_balance=0.00 - 0.00,
            #             notes="this is system generated",
            #         )
            if staff_charge:
                if staff_balance:
                    if (
                        staff_payment_1st_and_15th["total_payment"] is not None
                        and staff_time_charge_1st_and_15th["total_charge"] is not None
                    ):
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.filter(
                                staff=i, date=day_1st_and_15th
                            ).update(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=staff_payment_1st_and_15th[
                                    "total_payment"
                                ],
                                amount_due=staff_time_charge_1st_and_15th[
                                    "total_charge"
                                ],
                                account_balance=staff_payment_1st_and_15th[
                                    "total_payment"
                                ]
                                - staff_time_charge_1st_and_15th["total_charge"],
                            )
                    elif staff_payment_1st_and_15th["total_payment"] is None:
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.filter(
                                staff=i, date=day_1st_and_15th
                            ).update(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=Decimal(0.00),
                                amount_due=staff_time_charge_1st_and_15th[
                                    "total_charge"
                                ],
                                account_balance=Decimal(0.00)
                                - staff_time_charge_1st_and_15th["total_charge"],
                            )
                    elif staff_time_charge_1st_and_15th["total_charge"] is None:
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.filter(
                                staff=i, date=day_1st_and_15th
                            ).update(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=staff_payment_1st_and_15th[
                                    "total_payment"
                                ],
                                amount_due=staff_time_charge_1st_and_15th[
                                    "total_charge"
                                ],
                                account_balance=staff_payment_1st_and_15th[
                                    "total_payment"
                                ]
                                - staff_time_charge_1st_and_15th["total_charge"],
                            )
                    elif (
                        staff_payment_1st_and_15th["total_payment"] is None
                        and staff_time_charge_1st_and_15th["total_charge"] is None
                    ):
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.filter(
                                staff=i, date=day_1st_and_15th
                            ).update(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=Decimal(0.00),
                                amount_due=Decimal(0.00),
                                account_balance=Decimal(0.00),
                            )
                    if (
                        staff_payment_16th_and_31st["total_payment"] is not None
                        and staff_time_charge_16th_and_31st["total_charge"] is not None
                    ):
                        if today > every_16th and today < every_31st:
                            StaffAccountBalance.objects.filter(
                                staff=i, date__icontains=day_16th_and_31st
                            ).update(
                                payment_made=staff_payment_16th_and_31st[
                                    "total_payment"
                                ],
                                amount_due=staff_time_charge_16th_and_31st[
                                    "total_charge"
                                ],
                                account_balance=staff_payment_16th_and_31st[
                                    "total_payment"
                                ]
                                - staff_time_charge_16th_and_31st["total_charge"],
                                notes="This is system generated",
                            )
                    if (
                        staff_payment_16th_and_31st["total_payment"] is None
                        and staff_time_charge_16th_and_31st["total_charge"] is None
                    ):
                        if today > every_16th and today < every_31st:
                            StaffAccountBalance.objects.filter(
                                staff=i, date__icontains=day_16th_and_31st
                            ).update(
                                payment_made=Decimal(0.00),
                                amount_due=Decimal(0.00),
                                account_balance=Decimal(0.00) - Decimal(0.00),
                                notes="This is system generated",
                            )
                    elif staff_time_charge_16th_and_31st["total_charge"] is None:
                        if today > every_16th and today < every_31st:
                            StaffAccountBalance.objects.filter(
                                staff=i, date__icontains=day_16th_and_31st
                            ).update(
                                payment_made=Decimal(0.00),
                                amount_due=staff_time_charge_16th_and_31st[
                                    "total_charge"
                                ],
                                account_balance=staff_payment_16th_and_31st[
                                    "total_payment"
                                ]
                                - Decimal(0.00),
                                notes="this is system generated",
                            )
                    elif staff_payment_16th_and_31st["total_payment"] is None:
                        StaffAccountBalance.objects.filter(
                            staff=i, date__icontains=day_16th_and_31st
                        ).update(
                            payment_made=Decimal(0.00),
                            amount_due=staff_time_charge_16th_and_31st["total_charge"],
                            account_balance=Decimal(0.00)
                            - staff_time_charge_16th_and_31st["total_charge"],
                            notes="This is system generated",
                        )
                    elif (
                        staff_payment_16th_and_31st["total_payment"] is not None
                        and staff_time_charge_16th_and_31st["total_charge"] is not None
                    ):
                        StaffAccountBalance.objects.filter(
                            staff=i, date__icontains=day_16th_and_31st
                        ).update(
                            payment_made=staff_payment_16th_and_31st["total_payment"],
                            amount_due=staff_time_charge_16th_and_31st["total_charge"],
                            account_balance=staff_payment_16th_and_31st["total_payment"]
                            - staff_time_charge_16th_and_31st["total_charge"],
                            notes="this is created in create",
                        )
                else:
                    if (
                        staff_payment_1st_and_15th["total_payment"] is None
                        and staff_time_charge_1st_and_15th["total_charge"] is None
                    ):
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.create(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=0.00,
                                amount_due=0.00,
                                account_balance=0.00 - 0.00,
                                notes="this is system generated",
                            )
                    elif staff_payment_1st_and_15th["total_payment"] is None:
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.create(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=0.00,
                                amount_due=staff_time_charge_1st_and_15th[
                                    "total_charge"
                                ],
                                account_balance=0.00 - 0.00,
                                notes="this is system generated",
                            )
                    elif staff_time_charge_1st_and_15th["total_charge"] is None:
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.create(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=0.00,
                                amount_due=0.00,
                                account_balance=0.00
                                - staff_payment_1st_and_15th["total_payment"],
                                notes="this is system generated",
                            )
                    elif (
                        staff_payment_1st_and_15th["total_payment"] is not None
                        and staff_time_charge_1st_and_15th["total_charge"] is not None
                    ):
                        if today < every_15th and today > every_1st:
                            StaffAccountBalance.objects.create(
                                date=day_1st_and_15th,
                                staff=i,
                                payment_made=staff_payment_1st_and_15th[
                                    "total_payment"
                                ],
                                amount_due=staff_time_charge_1st_and_15th[
                                    "total_charge"
                                ],
                                account_balance=staff_payment_1st_and_15th[
                                    "total_payment"
                                ]
                                - staff_time_charge_1st_and_15th["total_charge"],
                                notes="this is system generated",
                            )
                    if (
                        staff_payment_16th_and_31st["total_payment"] is None
                        and staff_time_charge_16th_and_31st["total_charge"] is None
                    ):
                        if today > every_16th and today < every_31st:
                            StaffAccountBalance.objects.create(
                                date=day_16th_and_31st,
                                staff=i,
                                payment_made=Decimal(0.00),
                                amount_due=Decimal(0.00),
                                account_balance=Decimal(0.00) - Decimal(0.00),
                            )
                    elif staff_payment_16th_and_31st["total_payment"] is None:
                        if today > every_16th and today < every_31st:
                            StaffAccountBalance.objects.create(
                                date=day_16th_and_31st,
                                staff=i,
                                payment_made=Decimal(0.00),
                                amount_due=staff_time_charge_16th_and_31st[
                                    "total_charge"
                                ],
                                account_balance=Decimal(0.00)
                                - staff_time_charge_16th_and_31st["total_charge"],
                                notes="hehehe",
                            )
                    elif staff_time_charge_16th_and_31st["total_charge"] is None:
                        if today > every_16th and today < every_31st:
                            StaffAccountBalance.objects.create(
                                date=day_16th_and_31st,
                                staff=i,
                                payment_made=Decimal(0.00),
                                amount_due=staff_time_charge_16th_and_31st[
                                    "total_charge"
                                ],
                                account_balance=staff_payment_16th_and_31st[
                                    "total_payment"
                                ]
                                - Decimal(0.00),
                                notes="this is system generated",
                            )
                    elif (
                        staff_payment_16th_and_31st["total_payment"] is not None
                        and staff_time_charge_16th_and_31st["total_charge"] is not None
                    ):
                        StaffAccountBalance.objects.create(
                            date=day_16th_and_31st,
                            staff=i,
                            payment_made=staff_payment_16th_and_31st["total_payment"],
                            amount_due=staff_time_charge_16th_and_31st["total_charge"],
                            account_balance=staff_payment_16th_and_31st["total_payment"]
                            - staff_time_charge_16th_and_31st["total_charge"],
                            notes="this is created in create",
                        )

        if today < every_15th and today > every_1st:
            print("Staff balance is not updated")
        elif today > every_16th and today < every_31st:
            print("Staff balance is updated")
        print("Staff account balance created", today)