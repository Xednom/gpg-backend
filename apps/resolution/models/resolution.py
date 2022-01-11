from django.db import models

from django.contrib.auth import get_user_model

from apps.core.models import TimeStamped


User = get_user_model()


__all__ = ("Category", "Resolution", "ResolutionComment")


class StatusChoices(models.TextChoices):
    pending = "pending", ("Pending")
    in_progress = "in_progress", ("In progress")
    on_hold = "on_hold", ("On hold")
    closed = "closed", ("Closed")
    resolution_provided = "resolution_provided", ("Resolution provided")


class Category(TimeStamped):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name",)

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

    def __str__(self):
        return f"{self.client} - {self.category} - {self.description}"


class ResolutionComment(TimeStamped):
    resolution = models.ForeignKey(
        Resolution,
        related_name="resolution_comments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.resolution} - {self.comment}"
