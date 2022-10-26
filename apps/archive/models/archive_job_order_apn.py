from django.db import models

from apps.authentication.models import Client, Staff
from apps.core.models import TimeStamped
from apps.gpg.models import CategoryType, Deadline, PropertyDetail, JobOrderStatus


class ArchiveJobOrderApn(TimeStamped):
    ticket_number = models.CharField(max_length=100, blank=True)
    property_detail = models.ForeignKey(
        PropertyDetail,
        related_name="archive_property_details",
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        Client,
        related_name="archive_job_order_apn_clients",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    client_file = models.TextField(blank=True)
    client_email = models.EmailField(blank=True)
    staff = models.ManyToManyField(
        Staff,
        related_name="archive_job_order_apn_staffs",
        blank=True,
    )
    staff_email = models.EmailField(blank=True)
    category = models.ForeignKey(
        CategoryType,
        related_name="archive_job_order_categories",
        on_delete=models.CASCADE,
    )
    deadline = models.ForeignKey(
        Deadline, related_name="archive_job_order_deadline", on_delete=models.CASCADE
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