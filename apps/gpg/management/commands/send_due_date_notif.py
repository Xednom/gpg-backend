import datetime

from django.core.management.base import BaseCommand

from apps.gpg.models import JobOrderCategory, JobOrderGeneral
from post_office.models import EmailTemplate
from post_office import mail


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        emails = ""
        now = datetime.date.today()
        job_orders = (
            JobOrderGeneral.objects.all()
            .exclude(status="closed")
            .exclude(status="complete")
            .exclude(status="on_hold")
            .exclude(status="canceled")
            .exclude(status="duplicate_request")
            .exclude(status="dispute")
            .exclude(status="va_complete_multiple_task")
            .exclude(status="dd_call_out_complete")
            .exclude(status="initial_dd_complete")
        )
        job_order_apns = (
            JobOrderCategory.objects.all()
            .exclude(status="closed")
            .exclude(status="complete")
            .exclude(status="on_hold")
            .exclude(status="canceled")
            .exclude(status="duplicate_request")
            .exclude(status="dispute")
            .exclude(status="va_complete_multiple_task")
            .exclude(status="dd_call_out_complete")
            .exclude(status="initial_dd_complete")
        )
        email_template = EmailTemplate.objects.filter(name="due_date_notif").exists()

        for job in job_orders:
            days_before_posted = job.due_date - now
            days_after_posted = now - job.due_date
            if job.days_before_due_date:
                days_before_posted = job.due_date - job.created_at

                JobOrderGeneral.objects.filter(id=job.id).update(
                    days_before_due_date=days_before_posted.days,
                    days_after_due_date=days_after_posted.days,
                )
            if (
                job.days_before_due_date
                and email_template
                and job.staff_email
                and job.client_email
            ):
                emails = job.staff_email + " " + job.client_email
                emails = emails.split()
                mail.send(
                    "postmaster@landmaster.us",
                    bcc=emails,
                    template="due_date_notif",
                    context={"item": job},
                )

        for job in job_order_apns:
            days_before_posted = job.due_date - now
            days_after_posted = now - job.due_date

            if job.days_before_due_date:
                JobOrderCategory.objects.filter(id=job.id).update(
                    days_before_due_date=days_before_posted.days,
                    days_after_due_date=days_after_posted.days,
                )
            if (
                job.days_before_due_date
                and email_template
                and job.staff_email
                and job.client_email
            ):
                emails = job.staff_email + " " + job.client_email
                emails = emails.split()
                mail.send(
                    "postmaster@landmaster.us",
                    bcc=emails,
                    template="due_date_notif",
                    context={"item": job},
                )
