import datetime
import calendar

from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db.models import Sum, Q

from apps.core.models import Company, Vendor
from apps.operational_cost.models import (
    VendorExpense,
    CategoryExpense,
    OperationalCost,
    NetIncome,
)


class Command(BaseCommand):
    help = "Create expense"

    def handle(self, *args, **options):
        company_name = (
            OperationalCost.objects.all()
            .values_list("company_name", flat=True)
            .distinct()
        )
        vendor_name = (
            OperationalCost.objects.all().values_list("vendors", flat=True).distinct()
        )
        company = Company.objects.filter(id__in=company_name)
        vendor = Vendor.objects.filter(id__in=vendor_name)

        # automation for Company Expense
        for i in company:
            company_debit = OperationalCost.objects.filter(
                company_name__name=i.name, company_branch=i.branch
            ).aggregate(debit=Sum("debit"))
            company = Company.objects.filter(name=i.name, branch=i.branch).first()

            company_operating_cost = CategoryExpense.objects.filter(
                company__name=i.name
            ).exists()

            if company_operating_cost:
                CategoryExpense.objects.filter(company=company).update(
                    cost=company_debit["debit"], company=company
                )
            else:
                CategoryExpense.objects.create(
                    cost=company_debit["debit"],
                    company=company,
                )
        # automation for Vendor Expense
        for i in vendor:
            vendor_debit = OperationalCost.objects.filter(
                vendors__name=i.name
            ).aggregate(vendor_sum=Sum("debit"))
            vendor = Vendor.objects.filter(name=i.name).first()
            vendor_operating_cost = VendorExpense.objects.filter(
                vendor__name=i.name
            ).exists()

            if vendor_operating_cost:
                VendorExpense.objects.filter(vendor=vendor).update(
                    cost=vendor_debit["vendor_sum"], vendor=vendor
                )
            else:
                VendorExpense.objects.create(
                    cost=vendor_debit["vendor_sum"],
                    vendor=vendor,
                )

        # automation for Net Income
        today = datetime.datetime.now()
        month = str(calendar.month_abbr[today.month])
        year = str(today.year)
        month_year = str(calendar.month_abbr[today.month]) + "/" + str(today.year)
        net_income = NetIncome.objects.all()
        debit = OperationalCost.objects.filter(month=month).aggregate(
            debit=Sum("debit")
        )
        credit = OperationalCost.objects.filter(month=month).aggregate(
            credit=Sum("credit")
        )
        debit = OperationalCost.objects.filter(month=month).aggregate(
            debit=Sum("debit")
        )
        net = NetIncome.objects.filter(month_year=month_year).exists()

        if net:
            for i in net_income:
                total_net_income = debit["debit"] - credit["credit"]
                NetIncome.objects.filter(id=i.id, month_year=month_year).update(
                    debit=debit["debit"],
                    credit=credit["credit"],
                    net_income=total_net_income,
                )
        else:
            NetIncome.objects.create(
                month_year=month_year,
                debit=0.00,
                credit=0.00,
                net_income=0.00,
            )
