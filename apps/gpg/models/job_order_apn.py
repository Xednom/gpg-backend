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
    "Deadline",
    "JobOrderCategory",
    "CommentByApn",
    "State",
    "County",
)


class PropertyDetailStatus(models.TextChoices):
    sold = "sold", ("Sold")
    available = "available", ("Available")
    in_escrow = "in_escrow", ("In Escrow")
    in_contract = "in_contract", ("In Contract")
    ready_to_purchase = "ready_to_purchase", ("Ready to Purchase")
    ready_for_contract = "ready_for_contract", ("Ready for Contract")
    canceled_transaction = "canceled_transaction", ("Canceled Transaction")
    interested_to_purchase = "interested_to_purchase", ("Interested to purchase")
    need_of_research = "need_of_research", ("In need of research")
    not_applicable = "not_applicable", ("Not applicable")


class PropertyPriceStatus(models.TextChoices):
    deactivate = "deactivate", ("Deactivate")
    active = "active", ("Active")


class PropertyDetail(TimeStamped):
    ticket_number = models.CharField(max_length=150, blank=True)
    client = models.ForeignKey(
        Client,
        related_name="client_properties",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    staff = models.ManyToManyField(
        Staff, related_name="staff_assigned_properties", blank=True
    )
    property_status = models.CharField(
        choices=PropertyDetailStatus.choices, blank=True, max_length=25
    )
    client_email = models.CharField(max_length=100, blank=True)
    staff_email = models.CharField(max_length=100, blank=True)
    apn = models.CharField(max_length=250, unique=True)
    county = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    size = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    website_url = models.CharField(max_length=250, blank=True)
    file_storage = models.CharField(max_length=500, blank=True)
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

    def get_client_email(self):
        if self.client:
            email = self.client.user.email
            return email
        else:
            return ""

    def get_staff_email(self):
        if self.staff:
            staffs = Staff.objects.all()
            for staff in staffs:
                staff_emails = ' '.join(staff.company_email for staff in self.staff.all())
                return staff_emails

    def save(self, *args, **kwargs):
        if not self.id:
            self.ticket_number = self.create_ticket_number()
            super(PropertyDetail, self).save(*args, **kwargs)
        else:
            self.ticket_number = self.create_ticket_number()
            self.client_email = self.get_client_email()
            self.staff_email = self.get_staff_email()
            super(PropertyDetail, self).save(*args, **kwargs)


class CategoryType(TimeStamped):
    category = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.category}"


class PropertyPrice(TimeStamped):
    property_detail = models.ForeignKey(
        PropertyDetail, related_name="property_price_statuses", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="user_property_prices",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    asking_price = models.CharField(max_length=250)
    cash_terms = models.CharField(max_length=250)
    finance_terms = models.TextField()
    other_terms = models.TextField()
    price_status = models.CharField(
        max_length=30,
        choices=PropertyPriceStatus.choices,
        default=PropertyPriceStatus.active,
        blank=True,
    )
    notes = models.TextField()
    updated_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.property_detail}: status - {self.price_status}"


class Deadline(TimeStamped):
    deadline = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.deadline}"


class JobOrderCategory(TimeStamped):
    ticket_number = models.CharField(max_length=100, blank=True)
    property_detail = models.ForeignKey(
        PropertyDetail,
        related_name="apn_job_order_categories",
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        Client,
        related_name="client_jo_by_categories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    client_email = models.EmailField(blank=True)
    staff = models.ManyToManyField(
        Staff,
        related_name="staff_job_orders_by_categories",
        blank=True,
    )
    staff_email = models.EmailField(blank=True)
    category = models.ForeignKey(
        CategoryType, related_name="job_order_categories", on_delete=models.CASCADE
    )
    deadline = models.ForeignKey(
        Deadline, related_name="job_order_deadline", on_delete=models.CASCADE
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
    url_of_the_completed_jo = models.TextField(blank=True)
    notes_va = models.TextField(blank=True)
    notes_management = models.TextField(blank=True)
    total_time_consumed = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    class Meta:
        verbose_name_plural = "Job Order Categories"

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

    def get_client_email(self):
        if self.client:
            email = self.client.user.email
            return email
        else:
            return ""

    def get_staff_email(self):
        if self.staff:
            staffs = Staff.objects.all()
            for staff in staffs:
                staff_emails = ' '.join(staff.company_email for staff in self.staff.all())
                return staff_emails

    def save(self, *args, **kwargs):
        if not self.id:
            self.ticket_number = self.create_ticket_number()
            super(JobOrderCategory, self).save(*args, **kwargs)
        elif self.id:
            self.ticket_number = self.create_ticket_number()
            self.client_email = self.get_client_email()
            self.staff_email = self.get_staff_email()
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


class State(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class County(TimeStamped):
    name = models.CharField(max_length=250)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Counties"

    def __str__(self):
        return f"{self.name} - {self.state}"
