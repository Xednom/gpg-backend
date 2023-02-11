from django.db import models

from apps.core.models import TimeStamped, YesOrNoOrNotApplicable
from apps.forum.models import Status


__all__ = ("AssessmentFile",)


class AssessmentFile(TimeStamped):
    property_detail = models.ForeignKey(
        "gpg.PropertyDetail",
        related_name="property_detail_assessment_files",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    apn = models.CharField(max_length=250)
    client_code = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
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
    notes = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        "authentication.Staff",
        related_name="assessment_file_assigned_to",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    description_of_request = models.TextField(blank=True)
    completed_job_order_file = models.TextField(blank=True)
    date_completed = models.DateField(blank=True, null=True)
    status_of_job = models.CharField(max_length=25, choices=Status.choices, blank=True)
