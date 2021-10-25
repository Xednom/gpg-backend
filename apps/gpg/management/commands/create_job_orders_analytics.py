import calendar
import datetime

from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.gpg.models import JobOrderCategoryAnalytics, JobOrderCategory


class Command(BaseCommand):
    help = (
        "Automatically create Job Order Analytics for every user in the system monthly."
    )

    def handle(self, *args, **kwargs):

        today = datetime.datetime.now()
        month_year = str(calendar.month_abbr[today.month]) + "/" + str(today.year)
        print(today.month)
        client_name = (
            JobOrderCategory.objects.all().values_list("client", flat=True).distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            job_count = JobOrderCategory.objects.filter(
                client=i, created_at__month=today.month
            ).count()
            job_count_jan = JobOrderCategory.objects.filter(
                client=i, created_at__month="01"
            ).count()
            job_count_feb = JobOrderCategory.objects.filter(
                client=i, created_at__month="02"
            ).count()
            job_count_mar = JobOrderCategory.objects.filter(
                client=i, created_at__month="03"
            ).count()
            job_count_apr = JobOrderCategory.objects.filter(
                client=i, created_at__month="04"
            ).count()
            job_count_may = JobOrderCategory.objects.filter(
                client=i, created_at__month="05"
            ).count()
            job_count_jun = JobOrderCategory.objects.filter(
                client=i, created_at__month="06"
            ).count()
            job_count_jul = JobOrderCategory.objects.filter(
                client=i, created_at__month="07"
            ).count()
            job_count_aug = JobOrderCategory.objects.filter(
                client=i, created_at__month="08"
            ).count()
            job_count_sep = JobOrderCategory.objects.filter(
                client=i, created_at__month="09"
            ).count()
            job_count_oct = JobOrderCategory.objects.filter(
                client=i, created_at__month="10"
            ).count()
            job_count_nov = JobOrderCategory.objects.filter(
                client=i, created_at__month="11"
            ).count()
            job_count_dec = JobOrderCategory.objects.filter(
                client=i, created_at__month="11"
            ).count()
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
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Jan/2021",
                    client=i,
                    job_count=job_count_jan,
                    month="Jan",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Feb/2021",
                    client=i,
                    job_count=job_count_feb,
                    month="Feb",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Mar/2021",
                    client=i,
                    job_count=job_count_mar,
                    month="Mar",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Apr/2021",
                    client=i,
                    job_count=job_count_apr,
                    month="Apr",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="May/2021",
                    client=i,
                    job_count=job_count_may,
                    month="May",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Jun/2021",
                    client=i,
                    job_count=job_count_jun,
                    month="Jun",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Jul/2021",
                    client=i,
                    job_count=job_count_jul,
                    month="Jul",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Aug/2021",
                    client=i,
                    job_count=job_count_aug,
                    month="Aug",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Sep/2021",
                    client=i,
                    job_count=job_count_sep,
                    month="Sep",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Oct/2021",
                    client=i,
                    job_count=job_count_oct,
                    month="Oct",
                )
                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Nov/2021",
                    client=i,
                    job_count=job_count_nov,
                    month="Nov",
                )

                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year="Dec/2021",
                    client=i,
                    job_count=job_count_dec,
                    month="Dec",
                )

                job_count = JobOrderCategoryAnalytics.objects.create(
                    month_year=month_year,
                    client=i,
                    job_count=job_count,
                    month=str(calendar.month_abbr[today.month]),
                )
