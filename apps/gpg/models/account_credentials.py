from django.db import models

from apps.core.models import TimeStamped
from apps.authentication.models import Client, Staff


__all__ = ("AccountCredential",)


class AccessChoice(models.TextChoices):
    yes = "yes", ("Yes")
    no = "no", ("No")
    na = "na", ("N/A")


class AccountCredential(TimeStamped):
    client = models.ForeignKey(
        Client, related_name="client_accounts", on_delete=models.CASCADE
    )
    category = models.CharField(max_length=250)
    url = models.URLField()
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    notes = models.TextField(blank=True)
    granted_access_to = models.ForeignKey(
        Staff, related_name="staff_access", on_delete=models.CASCADE
    )
    access_granted = models.CharField(
        max_length=10, choices=AccessChoice.choices, default=AccessChoice.no
    )

    def __str__(self):
        return f"Account credentials for {self.client.client_name}"
