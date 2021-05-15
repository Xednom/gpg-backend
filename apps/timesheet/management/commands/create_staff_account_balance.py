import datetime

from decimal import Decimal

from django.db.models import Sum, Q
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
        staff_name = AccountCharge.objects.filter(status="approved").values_list("staff", flat=True).distinct()
        staff = Staff.objects.filter(id__in=staff_name)
        staff_timesheet = Staff.objects.filter(id__in=staff_name).exists()
        current_time = datetime.date.today()
        every_1st = datetime.date.today().replace(day=1)
        every_15th = datetime.date.today().replace(day=15)
        every_16th = datetime.date.today().replace(day=16)
        every_31st = datetime.date.today().replace(day=31)
        every_30th = datetime.date.today().replace(day=30)
        day_1st_and_15th = str(every_1st) + " " + str(every_15th)
        day_16th_and_30th = str(every_16th) + " " + str(every_30th)
        day_16th_and_31st = str(every_16th) + " " + str(every_31st)

        for i in staff:
            if staff_timesheet:
                staff_balance = StaffAccountBalance.objects.filter(staff=i).exists()
                staff_time_charge_1st_and_15th = AccountCharge.objects.filter(
                    staff=i, shift_date__gte=every_1st, shift_date__lte=every_15th
                ).aggregate(
                    totals=Sum("total_time"), total_charge=Sum("staff_total_due")
                )
                staff_time_charge_16th_and_30th = AccountCharge.objects.filter(
                    staff=i, shift_date__gte=every_16th, shift_date__lte=every_30th
                ).aggregate(
                    totals=Sum("total_time"), total_charge=Sum("staff_total_due")
                )
                staff_time_charge_16th_and_31st = AccountCharge.objects.filter(
                    staff=i, shift_date__gte=every_16th, shift_date__lte=every_31st
                ).aggregate(
                    totals=Sum("total_time"), total_charge=Sum("staff_total_due")
                )
                staff_payment_1st_and_15th = StaffPaymentHistory.objects.filter(
                    staff=i, date__range=[every_1st, every_15th]
                ).aggregate(total_payment=Sum("amount"))
                staff_payment_16th_and_31st = StaffPaymentHistory.objects.filter(
                    staff=i, date__gte=every_16th, date__lte=every_31st
                ).aggregate(total_payment=Sum("amount"))
                staff_payment_16th_and_30th = StaffPaymentHistory.objects.filter(
                    staff=i, date__gte=every_16th, date__lte=every_30th
                ).aggregate(total_payment=Sum("amount"))

                if every_15th == current_time:

                    if staff_payment_1st_and_15th["total_payment"] == None:
                        StaffAccountBalance.objects.create(
                            date=day_1st_and_15th,
                            staff=i,
                            payment_made=Decimal(0.00),
                            amount_due=staff_time_charge_1st_and_15th["total_charge"],
                            account_balance=Decimal(0.00)
                            - staff_time_charge_1st_and_15th["total_charge"],
                        )
                    else:
                        StaffAccountBalance.objects.create(
                            date=day_1st_and_15th,
                            staff=i,
                            payment_made=staff_payment_1st_and_15th["total_payment"],
                            amount_due=staff_time_charge_1st_and_15th["total_charge"],
                            account_balance=staff_payment_1st_and_15th["total_payment"]
                            - staff_time_charge_1st_and_15th["total_charge"],
                        )
                elif every_31st == current_time:
                    if staff_payment_16th_and_31st["total_payment"] == None:
                        StaffAccountBalance.objects.create(
                        date=day_16th_and_31st,
                        staff=i,
                        payment_made=Decimal(0.00),
                        amount_due=staff_time_charge_16th_and_31st["total_charge"],
                        account_balance=Decimal(0.00)
                        - staff_time_charge_16th_and_31st["total_charge"],
                    )
                    else:
                        StaffAccountBalance.objects.create(
                        date=day_16th_and_31st,
                        staff=i,
                        payment_made=staff_payment_16th_and_31st["total_payment"],
                        amount_due=staff_time_charge_16th_and_31st["total_charge"],
                        account_balance=staff_payment_16th_and_31st["total_payment"]
                        - staff_time_charge_16th_and_31st["total_charge"],
                    )
                elif every_30th == current_time:
                    if staff_payment_16th_and_30th["total_payment"] == None:
                        StaffAccountBalance.objects.create(
                        date=day_16th_and_30th,
                        staff=i,
                        payment_made=Decimal(0.00),
                        amount_due=staff_time_charge_16th_and_31st["total_charge"],
                        account_balance=Decimal(0.00)
                        - staff_time_charge_16th_and_31st["total_charge"],
                   )
                    else:
                        StaffAccountBalance.objects.create(
                        date=day_16th_and_30th,
                        staff=i,
                        payment_made=staff_payment_16th_and_30th["total_payment"],
                        amount_due=staff_time_charge_16th_and_31st["total_charge"],
                        account_balance=staff_payment_16th_and_30th["total_payment"]
                        - staff_time_charge_16th_and_31st["total_charge"],
                   )
