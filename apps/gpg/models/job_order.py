from django.db import models
from django.contrib.auth import get_user_model

from apps.core.models import TimeStamped
from apps.authentication.models import Client, Staff

User = get_user_model()


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
    request_for_job_order = "request_for_job_order", ("Request for job order")
    va_processing = "va_processing", ("VA Processing")
    management_processing = "management_processing", ("Management Processing")
    verified_job_order = "verified_job_order", ("Verified Job Order")
    on_hold = "on_hold", ("On Hold")
    canceled = "canceled", ("Canceled")
    follow_up = "follow_up", ("Follow up")
    dispute = "dispute", ("Dispute")
    complete = "complete", ("Complete")


class JobOrderGeneral(TimeStamped):
    client = models.ForeignKey(
        Client, related_name="clients_job_orders", on_delete=models.CASCADE
    )
    va_assigned = models.ForeignKey(
        Staff, related_name="vas_job_orders", on_delete=models.CASCADE
    )
    request_date = models.DateField()
    due_date = models.DateField()
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    client_notes = models.TextField()
    va_notes = models.TextField()
    status = models.CharField(
        max_length=100,
        choices=JobOrderStatus.choices,
        default=JobOrderStatus.na,
        blank=True,
    )
    date_completed = models.DateField()
    total_time_consumed = models.DecimalField(max_digits=10, decimal_places=2)


# TODO: confirmation for these models
# class PropertyDetails(TimeStamped):
#     client = models.ForeignKey(
#         Client, related_name="client_properties", on_delete=models.CASCADE
#     )
#     apn = models.CharField(max_length=250)
#     county = models.CharField(max_length=250)
#     state = models.CharField(max_length=250)
#     status = models.CharField(choices=Status.choices, blank=True, max_length=25)
#     size = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Property Details of {client.client_name}"


# class PropertyPrice(TimeStamped):
#     client = models.ForeignKey(
#         Client, related_name="property_prices", on_delete=models.CASCADE
#     )
#     asking_price = models.DecimalField(max_digits=11, decimal_places=2)
#     cash_terms = models.DecimalField(max_digits=11, decimal_places=2)
#     finance_terms = models.TextField()
#     other_terms = models.TextField()
#     notes = models.TextField()

#     def __str_(self):
#         return f"Property Price of {client.client_name} with price {self.askin_price}"


# class ListingAdDetails(TimeStamped):
#     category = models.CharField(
#         choices=ListingAdCategory.choices, max_length=30, blank=True
#     )
#     ad_details = models.TextField()
#     notes_client_side = models.TextField()
#     notes_va_side = models.TextField()
#     notes_management_side = models.TextField()

#     def __str__(self):
#         return f"Listing Ad details of {client.client_name}"


# class ApprovedOfferNotes(TimeStamped):
#     client = models.ForeignKey(
#         Client, related_name="approved_offer_notes", on_delete=models.CASCADE
#     )
#     asking_price = models.DecimalField(max_digits=11, decimal_places=2)
#     cash_terms = models.DecimalField(max_digits=11, decimal_places=2)
#     finance_terms = models.TextField()
#     other_terms = models.TextField()
#     notes = models.TextField()

#     def __str_(self):
#         return f"Approved offer notes of {client.client_name} with price {self.askin_price}"


# class LeadManagement(TimeStamped):
#     date_lead_added = models.DateField()
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     phone = models.CharField(max_length=30)
#     email = models.EmailField()
#     lead_source = models.CharField(max_length=250)
#     lead_status = models.CharField(
#         choices=LeadStatus.choices, max_length=50, blank=True
#     )
#     date_of_callback = models.DateField()
#     time = models.TimeField()
#     call_center_rep_notes = models.TextField()
#     call_center_reps_id = models.CharField(max_length=100)
#     lead_added_by = models.CharField(max_length=250)

#     def __str__(self):
#         return f"Lead added by {self.lead_added_by}"


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
        ordering = ["-created_at"]
