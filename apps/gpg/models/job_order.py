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
    job_order_request = "job_order_request", ("Job order request")
    va_processing = "va_processing", ("VA Processing")
    management_processing = "management_processing", ("Management Processing")
    verified_job_order = "verified_job_order", ("Verified Job Order")
    on_hold = "on_hold", ("On Hold")
    canceled = "canceled", ("Canceled")
    follow_up = "follow_up", ("Follow up")
    dispute = "dispute", ("Dispute")
    complete = "complete", ("Complete")


class PropertyPriceStatus(models.TextChoices):
    change = "change", ("Change")
    active = "active", ("Active")


class JobOrderGeneral(TimeStamped):
    client = models.ForeignKey(
        Client,
        related_name="clients_job_orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    va_assigned = models.ForeignKey(
        Staff,
        related_name="vas_job_orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
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

    def save(self, *args, **kwargs):
        self.ticket_number = self.create_ticket_number()
        super(JobOrderGeneral, self).save(*args, **kwargs)


class PropertyDetail(TimeStamped):
    ticket_number = models.CharField(max_length=150, blank=True)
    client = models.ForeignKey(
        Client, related_name="client_properties", on_delete=models.CASCADE
    )
    apn = models.CharField(max_length=250)
    county = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    status = models.CharField(choices=Status.choices, blank=True, max_length=25)
    size = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Property Details of {self.client.client_name}"
    
    def create_ticket_number(self):
        ticket_code = ""
        last_in = PropertyDetail.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            ticket_number = "PD000" + str((int(seq) + 1))
            return ticket_number

        if self.id:
            ticket_number = "PD000" + str(self.id)
            return ticket_number

        in_id = last_in.id
        in_int = int(in_id)
        ticket_code = "PD000" + str(int(in_int) + 1)
        return ticket_code

    def save(self, *args, **kwargs):
        self.ticket_number = self.create_ticket_number()
        super(PropertyDetail, self).save(*args, **kwargs)


class PropertyPrice(TimeStamped):
    property_details = models.ForeignKey(
        PropertyDetail, related_name="property_prices", on_delete=models.CASCADE
    )
    asking_price = models.DecimalField(max_digits=11, decimal_places=2)
    cash_terms = models.DecimalField(max_digits=11, decimal_places=2)
    finance_terms = models.TextField()
    other_terms = models.TextField()
    notes = models.TextField()
    status = models.CharField(
        max_length=30,
        choices=PropertyPriceStatus.choices,
        default=PropertyPriceStatus.active,
        blank=True,
    )

    def __str_(self):
        return f"{client.client_name} with asking price {self.asking_price}"


class ListingAdDetail(TimeStamped):
    property_details = models.ForeignKey(
        PropertyDetail, related_name="listing_ads", on_delete=models.CASCADE
    )
    category = models.CharField(
        choices=ListingAdCategory.choices, max_length=30, blank=True
    )
    ad_details = models.TextField()
    notes_client_side = models.TextField()
    notes_va_side = models.TextField()
    notes_management_side = models.TextField()

    def __str__(self):
        return f"{self.property_details} with {self.ad_details}"


class CategoryType(TimeStamped):
    category = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.category}"


class JobOrderCategory(TimeStamped):
    ticket_number = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(
        CategoryType, related_name="job_order_categories", on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=100,
        choices=JobOrderStatus.choices,
        default=JobOrderStatus.na,
        blank=True,
    )
    due_date = models.DateField()
    date_completed = models.DateField(blank=True, null=True)
    job_description = models.TextField()
    completed_url_work = models.URLField(blank=True)
    va_assigned = models.ForeignKey(
        Staff,
        related_name="vas_job_orders_by_categories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    notes_va = models.TextField(blank=True)
    notes_management = models.TextField(blank=True)
    total_time_consumed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Job order by {self.category}"
    
    def create_ticket_number(self):
        ticket_code = ""
        last_in = JobOrderCategory.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            ticket_number = "JOC000" + str((int(seq) + 1))
            return ticket_number

        if self.id:
            ticket_number = "JOC000" + str(self.id)
            return ticket_number

        in_id = last_in.id
        in_int = int(in_id)
        ticket_code = "JOC000" + str(int(in_int) + 1)
        return ticket_code

    def save(self, *args, **kwargs):
        self.ticket_number = self.create_ticket_number()
        super(JobOrderCategory, self).save(*args, **kwargs)


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


class CommentByPropertDetail(TimeStamped):
    property_details = models.ForeignKey(
        PropertyDetail,
        related_name="property_detail_comments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        ordering = ["created_at"]
