from django.db import models
from django.contrib.auth import get_user_model

from apps.core.models import TimeStamped
from apps.authentication.models import Client, Staff

User = get_user_model()


__all__ = (
    "Status",
    "ListingAdCategory",
    "LeadStatus",
    "JobOrderStatus",
    "JobOrderGeneral",
    "Comment",
)


class Status(models.TextChoices):
    sold = "sold", ("Sold")
    available = "available", ("Available")
    in_escrow = "in_escrow", ("In Escrow")
    in_contract = "in_contract", ("In Contract")
    ready_to_purchase = "ready_to_purchase", ("Ready to Purchase")
    ready_for_contract = "ready_for_contract", ("Ready for Contract")
    canceled_transaction = "canceled_transaction", ("Canceled Transaction")


class ListingAdCategory(models.TextChoices):
    company_name = "company_name", ("Company Name")
    phone = "phone", ("Phone")
    email_ad = "email_ad", ("Email Ad")
    website_url = "website_url", ("Website URL")


class LeadStatus(models.TextChoices):
    interested = "interested", ("Interested")
    ask_additional_info = "ask_additional_info", ("Ask for additional info")
    ask_for_callback = "ask_for_callback", ("Ask for callback")
    follow_up_call = "follow_up_call", ("Follow up Call")
    others = "others", ("Others")


class JobOrderStatus(models.TextChoices):
    na = "na", ("N/A")
    job_order_request = "job_order_request", ("Job order request")
    va_processing = "va_processing", ("VA Processing")
    management_processing = "management_processing", ("Management Processing")
    verified_job_order = "verified_job_order", ("Verified Job Order")
    on_hold = "on_hold", ("On Hold")
    canceled = "canceled", ("Canceled")
    follow_up = "follow_up", ("Follow up")
    dispute = "dispute", ("Dispute")
    complete = "complete", ("Complete")
    under_quality_review = "under_quality_review", ("Under Quality Review")


class JobOrderGeneral(TimeStamped):
    client = models.ForeignKey(
        Client,
        related_name="clients_job_orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    client_email = models.EmailField(blank=True)
    va_assigned = models.ForeignKey(
        Staff,
        related_name="vas_job_orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    staff_email = models.EmailField(blank=True)
    ticket_number = models.CharField(max_length=100, blank=True)
    request_date = models.DateField()
    due_date = models.DateField()
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    client_notes = models.TextField(blank=True)
    va_notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=100,
        choices=JobOrderStatus.choices,
        default=JobOrderStatus.na,
        blank=True,
    )
    date_completed = models.DateField(blank=True, null=True)
    total_time_consumed = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    class Meta:
        ordering = ["-ticket_number"]

    def create_ticket_number(self):
        ticket_code = ""
        last_in = JobOrderGeneral.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            ticket_number = "JO000" + str((int(seq) + 1))
            return ticket_number

        if self.id:
            ticket_number = "JO000" + str(self.id)
            return ticket_number

        in_id = last_in.id
        in_int = int(in_id)
        ticket_code = "JO000" + str(int(in_int) + 1)
        return ticket_code
    
    def get_client_email(self):
        if self.client:
            email = self.client.user.email
            return email
    
    def get_staff_email(self):
        if self.va_assigned:
            email = self.va_assigned.user.email
            return email

    def save(self, *args, **kwargs):
        self.ticket_number = self.create_ticket_number()
        self.client_email = self.get_client_email()
        self.staff_email = self.get_staff_email()
        super(JobOrderGeneral, self).save(*args, **kwargs)


class Comment(TimeStamped):
    job_order = models.ForeignKey(
        JobOrderGeneral,
        related_name="job_order_comments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        ordering = ["created_at"]
