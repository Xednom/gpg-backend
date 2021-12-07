from django.db import models

from apps.core.models import TimeStamped


__all__ = ("Category", "Resolution")


class StatusChoices(models.TextChoices):
    pending = "pending", ("Pending")
    in_progress = "in_progress", ("In progress")
    on_hold = "on_hold", ("On hold")
    closed = "closed", ("Closed")
    resolution_provided = "resolution_provided", ("Resolution provided")


class Category(TimeStamped):
    name = models.CharField(max_length=255)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "-"


class Resolution(TimeStamped):
    date_submitted = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        "authentication.Staff", on_delete=models.SET_NULL, blank=True, null=True
    )
    client = models.ForeignKey(
        "authentication.Client", on_delete=models.SET_NULL, blank=True, null=True
    )
    resolution_provided_by_management = models.TextField(blank=True)
    status = models.CharField(
        max_length=255, choices=StatusChoices.choices, default=StatusChoices.pending
    )
    additional_notes = models.TextField(blank=True)
