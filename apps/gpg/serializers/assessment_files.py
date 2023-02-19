from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.gpg.models import AssessmentFile, PropertyDetail
from apps.authentication.models import Staff

__all__ = ("AssessmentFileSerializer",)


class AssessmentFileSerializer(WritableNestedModelSerializer):
    property_detail = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        allow_null=True,
        required=False,
        queryset=PropertyDetail.objects.all(),
    )

    assigned_to = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        allow_null=True,
        required=False,
        queryset=Staff.objects.all(),
    )

    class Meta:
        model = AssessmentFile
        fields = (
            "property_detail",
            "apn",
            "client_code",
            "description",
            "packets",
            "comps_by_parcel",
            "comps_by_area",
            "due_diligence",
            "notes",
            "assigned_to",
            "description_of_request",
            "completed_job_order_file",
            "date_completed",
            "status_of_job",
        )
