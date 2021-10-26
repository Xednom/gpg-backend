import calendar
import datetime

from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.gpg.models import (
    JobOrderCategoryAnalytics,
    JobOrderCategory,
    JobOrderGeneral,
    JobOrderGeneralAnalytics,
)


class Command(BaseCommand):
    help = (
        "Automatically create Job Order Analytics for every user in the system monthly."
    )

    def handle(self, *args, **kwargs):

        today = datetime.datetime.now()
        month_year = str(calendar.month_abbr[today.month]) + "/" + str(today.year)
        client_name = (
            JobOrderCategory.objects.all().values_list("client", flat=True).distinct()
        )
        job_order_general_client_name = (
            JobOrderGeneral.objects.all().values_list("client", flat=True).distinct()
        )
        client_job_order_general = Client.objects.filter(
            id__in=job_order_general_client_name
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            job_count = JobOrderCategory.objects.filter(
                client=i, created_at__month=today.month
            ).count()
            # job_count_jan = JobOrderCategory.objects.filter(
            #     client=i, created_at__month="01"
            # ).count()
            job_created = JobOrderCategoryAnalytics.objects.filter(
                client=i, month_year=month_year
            ).exists()

            if job_created:
                job_count = JobOrderCategoryAnalytics.objects.filter(
                    client=i, month_year=month_year
                ).update(
                    month_year=month_year,
                    client=i,
                    job_count=job_count,
                    month=str(calendar.month_abbr[today.month]),
                )

            else:
                # job_count = JobOrderCategoryAnalytics.objects.create(
                #     month_year="Jan/2021",
                #     client=i,
                #     job_count=job_count_jan,
                #     month="Jan",
                # )

                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year=month_year,
                    client=i,
                    job_count=job_count,
                    month=str(calendar.month_abbr[today.month]),
                )

        for i in client_job_order_general:
            job_count = JobOrderGeneral.objects.filter(
                client=i, created_at__month=today.month
            ).count()

            job_order_general_created = JobOrderGeneralAnalytics.objects.filter(
                client=i, month_year=month_year
            ).exists()

            # job_count_jan = JobOrderGeneral.objects.filter(
            #     client=i, created_at__month="01"
            # ).count()

            if job_order_general_created:
                job_count = JobOrderGeneralAnalytics.objects.filter(
                    client=i, month_year=month_year
                ).update(
                    month_year=month_year,
                    client=i,
                    job_count=job_count,
                    month=str(calendar.month_abbr[today.month]),
                )

            else:
                # job_count = JobOrderGeneralAnalytics.objects.create(
                #     month_year="Jan/2021",
                #     client=i,
                #     job_count=job_count_jan,
                #     month="Jan",
                # )
                job_count = JobOrderGeneralAnalytics.objects.create(
                    month_year=month_year,
                    client=i,
                    job_count=job_count,
                    month=str(calendar.month_abbr[today.month]),
                )
