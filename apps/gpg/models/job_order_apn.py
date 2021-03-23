from django.db import models
from django.contrib.auth import get_user_model

from apps.core.models import TimeStamped
from apps.authentication.models import Client, Staff
from .job_order import JobOrderStatus, Status, ListingAdCategory

User = get_user_model()


__all__ = (
    "PropertyPriceStatus",
    "PropertyDetail",
    "PropertyPrice",
    "CategoryType",
    "JobOrderCategory",
    "CommentByApn",
)


class PropertyPriceStatus(models.TextChoices):
    change = "change", ("Change")
    active = "active", ("Active")


class PropertyDetail(TimeStamped):
    ticket_number = models.CharField(max_length=150, blank=True)
    client = models.ForeignKey(
        Client, related_name="client_properties", on_delete=models.CASCADE,
        blank=True, null=True
    )
    staff = models.ForeignKey(
        Staff, related_name="staff_assigned_properties", on_delete=models.CASCADE,
        blank=True, null=True
    )
    property_status = models.CharField(
        choices=Status.choices, blank=True, max_length=25
    )
    apn = models.CharField(max_length=250, unique=True)
    county = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    size = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    website_url = models.CharField(max_length=250, blank=True)
    ad_details = models.TextField(blank=True)
    notes_client_side = models.TextField(blank=True)
    notes_va_side = models.TextField(blank=True)
    notes_management_side = models.TextField(blank=True)

    def __str__(self):
        return f"{self.apn}"

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


class CategoryType(TimeStamped):
    category = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.category}"


class PropertyPrice(TimeStamped):
    property_detail = models.ForeignKey(PropertyDetail, related_name="property_price_statuses", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_property_prices", on_delete=models.CASCADE, blank=True, null=True)
    asking_price = models.CharField(max_length=250)
    cash_terms = models.CharField(max_length=250)
    finance_terms = models.CharField(max_length=250)
    other_terms = models.CharField(max_length=250)
    price_status = models.CharField(
        max_length=30,
        choices=PropertyPriceStatus.choices,
        default=PropertyPriceStatus.active,
        blank=True,
    )
    notes = models.TextField()
    updated_info = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.property_detail}: status - {self.price_status}"


class JobOrderCategory(TimeStamped):
    ticket_number = models.CharField(max_length=100, blank=True)
    property_detail = models.ForeignKey(PropertyDetail, related_name="apn_job_order_categories", on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, related_name="client_jo_by_categories", on_delete=models.CASCADE, blank=True,
        null=True,
    )
    staff = models.ForeignKey(
        Staff,
        related_name="staff_job_orders_by_categories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
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
    notes_va = models.TextField(blank=True)
    notes_management = models.TextField(blank=True)
    total_time_consumed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

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


class CommentByApn(TimeStamped):
    job_order_category = models.ForeignKey(
        JobOrderCategory,
        related_name="job_order_category_comments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        ordering = ["created_at"]
