from django.db import models

from apps.core.models import TimeStamped


__all__ = ("JobOrderGeneralRating", "JobOrderCategoryRating")


class JobOrderGeneralRating(TimeStamped):
    """
    Job General Rating
    """

    job_order = models.ForeignKey(
        "gpg.JobOrderGeneral",
        on_delete=models.CASCADE,
        related_name="job_general_ratings",
        null=True,
        blank=True,
    )
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    client = models.ForeignKey(
        "authentication.Client",
        on_delete=models.CASCADE,
        related_name="job_order_general_rating_clients",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Job Rating"
        verbose_name_plural = "Job Ratings"

    def __str__(self):
        return f"{self.job_order} - {self.rating}"


class JobOrderCategoryRating(TimeStamped):
    """
    Job Category Rating
    """

    job_order = models.ForeignKey(
        "gpg.JobOrderGeneral",
        on_delete=models.CASCADE,
        related_name="job_category_ratings",
        null=True,
        blank=True,
    )
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    client = models.ForeignKey(
        "authentication.Client",
        on_delete=models.CASCADE,
        related_name="job_order_category_rating_clients",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Job Category Rating"
        verbose_name_plural = "Job Category Ratings"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.job_order} - {self.rating}"

