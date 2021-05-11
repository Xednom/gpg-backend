from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.timesheet.models import AccountCharge, PaymentHistory, AccountBalance


class Command(BaseCommand):
    help = "Automatically create Account balance for every user in the system monthly."

    def handle(self, *args, **kwargs):
        client_name = AccountCharge.objects.filter(status="approved").values_list("client", flat=True).distinct()
        client = Client.objects.filter(id__in=client_name)
        account_balance_deficit = AccountBalance.objects.filter(
            account_balance__lte=0.00
        )

        for i in client:
            client_balance = AccountBalance.objects.filter(client=i).exists()
            client_time_charge = (
                AccountCharge.objects.filter(client=i, status="approved")
                .aggregate(
                    totals=Sum("total_time"),
                    total_charge=Sum("client_total_charge"),
                    total_due=Sum("client_total_due"),
                )
            )
            client_payment = PaymentHistory.objects.filter(client=i).aggregate(
                total_payment=Sum("amount")
            )

            if client_payment["total_payment"] == None:
                if client_balance:
                    AccountBalance.objects.filter(client=i).update(
                        total_payment_made=Decimal(0.00),
                        total_time_consumed=client_time_charge["totals"],
                        account_charges=client_time_charge["total_due"],
                        account_balance=Decimal(0.00)
                        - client_time_charge["total_due"],
                    )

                else:
                    AccountBalance.objects.create(
                        client=i,
                        total_payment_made=Decimal(0.00),
                        total_time_consumed=client_time_charge["totals"],
                        account_charges=client_time_charge["total_due"],
                        account_balance=Decimal(0.00)
                        - client_time_charge["total_due"],
                    )
            else:
                if client_balance:
                    AccountBalance.objects.filter(client=i).update(
                        total_payment_made=client_payment["total_payment"],
                        total_time_consumed=client_time_charge["totals"],
                        account_charges=client_time_charge["total_due"],
                        account_balance=client_payment["total_payment"]
                        - client_time_charge["total_due"],
                    )

                else:
                    AccountBalance.objects.create(
                        client=i,
                        total_payment_made=client_payment["total_payment"],
                        total_time_consumed=client_time_charge["totals"],
                        account_charges=client_time_charge["total_due"],
                        account_balance=client_payment["total_payment"]
                        - client_time_charge["total_due"],
                    )

        for i in account_balance_deficit:

            if account_balance_deficit:
                mail.send(
                    i.client.user.email,
                    template="account_balance_deficit",
                    context={"account_balance": i},
                )
