from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.gpg.models import Acquisition, PropertyDetail
from apps.authentication.models import Staff

__all__ = ("AcquisitionSerializer",)


class AcquisitionSerializer(WritableNestedModelSerializer):
    property_detail = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        allow_null=True,
        required=False,
        queryset=PropertyDetail.objects.all(),
    )

    assigned_sales_team = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        allow_null=True,
        required=False,
        queryset=Staff.objects.all(),
    )

    class Meta:
        model = Acquisition
        fields = (
            "property_detail",
            "apn",
            "possible_offer",
            "approved_amount_from_client",
            "minimum_amount",
            "maximum_amount",
            "amount_closed_deal",
            "deal_status",
            "assigned_sales_team",
            "notes",
        )
