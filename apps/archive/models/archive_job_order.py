from sqlite3 import Timestamp
from django.db import models

from apps.core.models import TimeStamped
from apps.authentication.models import Client, Staff
from apps.gpg.models.job_order import JobOrderStatus


class ArchiveJobOrder(TimeStamped):
    client = models.ForeignKey(
        Client,
        related_name="archive_job_order_clients",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    client_file = models.TextField(blank=True)
    client_email = models.EmailField(blank=True)
    va_assigned = models.ManyToManyField(
        Staff, related_name="archive_job_orders_va_assigns", blank=True
    )
    staff_email = models.TextField(blank=True)
    ticket_number = models.CharField(max_length=100, blank=True)
    request_date = models.DateField()
    due_date = models.DateField()
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    client_notes = models.TextField(blank=True)
    va_notes = models.TextField(blank=True)
    management_notes = models.TextField(blank=True)
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
    url_of_the_completed_jo = models.TextField(blank=True)
