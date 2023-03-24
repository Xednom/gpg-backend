from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.gpg.models import ListingFile, PropertyDetail, ListingStatus
from apps.authentication.models import Staff

__all__ = ("ListingFileSerializer", "ListingStatusSerializer")


class ListingStatusSerializer(WritableNestedModelSerializer):
    class Meta:
        model = ListingStatus
        fields = (
            "id",
            "name",
        )


class ListingFileSerializer(WritableNestedModelSerializer):
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
    listing_status = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        allow_null=True,
        required=False,
        queryset=ListingStatus.objects.all(),
    )
    listing_status__name = serializers.SerializerMethodField()

    class Meta:
        model = ListingFile
        fields = (
            "id",
            "property_detail",
            "apn",
            "client_code",
            "description",
            "tagging",
            "listing_sites",
            "notes",
            "assigned_to",
            "description_of_request",
            "completed_job_order_file",
            "date_completed",
            "status_of_job",
            "listing_status",
            "listing_status__name",
        )

    def get_listing_status__name(self, instance):
        if instance.listing_status:
            print("Listing status name: ", instance.listing_status.name)
            return instance.listing_status.name
