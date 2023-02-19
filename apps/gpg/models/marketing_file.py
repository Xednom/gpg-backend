from django.db import models

from apps.core.models import TimeStamped, FileModel, YesOrNoOrNotApplicable
from apps.forum.models import Status


__all__ = ("MarketingFile",)


class MarketingFile(FileModel):
    property_detail = models.ForeignKey(
        "gpg.PropertyDetail",
        related_name="property_detail_marketing_file",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    assigned_to = models.ForeignKey(
        "authentication.Staff",
        related_name="marketing_file_assigned_to",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    images = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )
    ad_content = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )
    youtube_videos = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )
    tiktok_videos = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )
    email_campaign = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )
    other_graphics = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )
    other_makerting_files = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )
    neighbor_list = models.CharField(
        max_length=25,
        choices=YesOrNoOrNotApplicable.choices,
        default=YesOrNoOrNotApplicable.not_applicable,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
