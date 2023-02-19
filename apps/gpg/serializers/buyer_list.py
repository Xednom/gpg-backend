from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.gpg.models import BuyerList, PropertyDetail
from apps.authentication.models import Staff

__all__ = ("BuyerListSerializer",)


class BuyerListSerializer(WritableNestedModelSerializer):
    property_detail = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        allow_null=True,
        required=False,
        queryset=PropertyDetail.objects.all(),
    )

    lead_assigned_to = PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        allow_null=True,
        required=False,
        queryset=Staff.objects.all(),
    )

    class Meta:
        model = BuyerList
        fields = (
            "property_detail",
            "apn",
            "client_code",
            "date_lead_added",
            "lead_type",
            "buyer_lead_name",
            "phone_number",
            "email",
            "lead_status",
            "buyer_offer",
            "counter_offer_amount",
            "lead_assigned_to",
            "total_minutes_consumed",
            "notes",
        )
