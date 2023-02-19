from django.db import models

from apps.core.models import TimeStamped, FileModel, YesOrNoOrNotApplicable
from apps.forum.models import Status


__all__ = ("ListingStatus", "ListingFile")


class ListingStatus(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Listing Status"
        verbose_name_plural = "Listing Statuses"


class ListingFile(FileModel):
    property_detail = models.ForeignKey(
        "gpg.PropertyDetail",
        related_name="property_detail_listing_file",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    assigned_to = models.ForeignKey(
        "authentication.Staff",
        related_name="listing_file_assigned_to",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    tagging = models.CharField(max_length=250, blank=True)
    listing_sites = models.CharField(max_length=250, blank=True)
    listing_status = models.ForeignKey(
        ListingStatus,
        related_name="listing_file_listing_status",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-created_at"]
