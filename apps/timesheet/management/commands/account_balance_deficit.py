import datetime
from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.timesheet.models import AccountBalance


class Command(BaseCommand):
    help = "Automatically create Account balance for every user in the system monthly."

    def handle(self, *args, **kwargs):
        account_balance_deficit = AccountBalance.objects.filter(
            account_balance__range=[0.00, 49.00]
        ) or AccountBalance.objects.filter(account_balance__lte=0.00)
        now = datetime.datetime.now()
        if account_balance_deficit:
            for i in account_balance_deficit:
                if now.strftime("%A") == "Tuesday":

                    mail.send(
                        i.client.user.email,
                        template="account_balance_deficit",
                        context={"account_balance": i},
                    )
