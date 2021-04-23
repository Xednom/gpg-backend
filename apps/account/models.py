from django.db import models

from apps.core.models import TimeStamped
from apps.authentication.models import Client, Staff


class LoginCredential(TimeStamped):
    client = models.ForeignKey(
        Client,
        related_name="client_logins",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    category = models.CharField(max_length=250, blank=True)
    url = models.URLField(max_length=500, blank=True)
    username = models.CharField(max_length=250, blank=True)
    password = models.CharField(max_length=250, blank=True)
    notes = models.TextField(blank=True)
    staff = models.ManyToManyField(
        Staff,
        related_name="login_assigned_staffs",
        blank=True
    )

    def __str__(self):
        return f"{self.client} - {self.category}"
