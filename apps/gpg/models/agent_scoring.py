from sqlite3 import Time
from django.db import models
from django.contrib.auth import get_user_model

from apps.core.models import TimeStamped

User = get_user_model()


__all__ = ("JobOrderGeneralAgentScoring", "JobOrderCategoryAgentScoring")


class JobOrderGeneralAgentScoring(TimeStamped):
    staff = models.ManyToManyField(
        "authentication.Staff",
        related_name="job_order_general_staff_scorings",
        blank=True,
    )
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_agent_scorings",
        on_delete=models.CASCADE,
    )
    job_order_general = models.ForeignKey(
        "gpg.jobOrderGeneral",
        related_name="job_order_general_scorings",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    accuracy = models.IntegerField()
    speed = models.IntegerField()
    quality_of_work = models.IntegerField()
    delivered_on_time = models.BooleanField(default=False)
    delivery_note = models.TextField(blank=True)
    job_completed = models.BooleanField(default=False)
    job_completed_note = models.TextField(
        blank=True,
        help_text="Was the job completed based on your instruction or expectations?",
    )
    satisfied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff}'s rate for {self.job_order_general}"


class JobOrderCategoryAgentScoring(TimeStamped):
    staff = models.ManyToManyField(
        "authentication.Staff",
        related_name="job_order_category_staff_scorings",
        blank=True,
    )
    client = models.ForeignKey("authentication.Client", on_delete=models.CASCADE)
    job_order_category = models.ForeignKey(
        "gpg.jobOrderCategory", related_name="job_order_category_scorings", on_delete=models.CASCADE, blank=True, null=True
    )
    accuracy = models.IntegerField()
    speed = models.IntegerField()
    quality_of_work = models.IntegerField()
    delivered_on_time = models.BooleanField(default=False)
    delivery_note = models.TextField(blank=True)
    job_completed = models.BooleanField(default=False)
    job_completed_note = models.TextField(
        blank=True,
        help_text="Was the job completed based on your instruction or expectations?",
    )
    satisfied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff}'s rate for {self.job_order_category}"
