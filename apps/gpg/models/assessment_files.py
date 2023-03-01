from django.db import models

from apps.core.models import FileModel, YesOrNoOrNotApplicable
from apps.forum.models import Status


__all__ = ("AssessmentFile",)


class AssessmentFile(FileModel):
    property_detail = models.ForeignKey(
        "gpg.PropertyDetail",
        related_name="property_detail_assessment_files",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    packets = models.CharField(
        max_length=25, choices=YesOrNoOrNotApplicable.choices, blank=True
    )
    comps_by_parcel = models.CharField(
        max_length=25, choices=YesOrNoOrNotApplicable.choices, blank=True
    )
    comps_by_area = models.CharField(
        max_length=25, choices=YesOrNoOrNotApplicable.choices, blank=True
    )
    due_diligence = models.CharField(
        max_length=25, choices=YesOrNoOrNotApplicable.choices, blank=True
    )
    assigned_to = models.ForeignKey(
        "authentication.Staff",
        related_name="assessment_file_assigned_to",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
