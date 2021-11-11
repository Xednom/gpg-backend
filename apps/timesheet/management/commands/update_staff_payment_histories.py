import datetime
from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from apps.authentication.models import Staff, User
from apps.timesheet.models import StaffPaymentHistory


class Command(BaseCommand):
    help = "Automatically create Account balance for every user in the system monthly."

    def handle(self, *args, **kwargs):
        staff_name = Staff.objects.all()
        staff = Staff.objects.filter(id__in=staff_name)
        for i in staff:
            if i.user:
                staff = StaffPaymentHistory.objects.filter(staff=i).update(
                    company_name=i.user.company_category
                )
