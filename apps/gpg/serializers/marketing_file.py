from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.gpg.models import MarketingFile, PropertyDetail
from apps.authentication.models import Staff

__all__ = ("MarketingFileSerializer",)


class MarketingFileSerializer(WritableNestedModelSerializer):
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
        model = MarketingFile
        fields = (
            "id",
            "property_detail",
            "apn",
            "client_code",
            "description",
            "images",
            "ad_content",
            "youtube_videos",
            "tiktok_videos",
            "email_campaign",
            "other_graphics",
            "other_makerting_files",
            "neighbor_list",
            "notes",
            "assigned_to",
            "description_of_request",
            "completed_job_order_file",
            "date_completed",
            "status_of_job",
        )
