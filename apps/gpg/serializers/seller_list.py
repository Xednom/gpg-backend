from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.gpg.models import SellerList, PropertyDetail, CounterOffer
from apps.authentication.models import Staff

__all__ = ("SellerListSerializer",)


class SellerListSerializer(WritableNestedModelSerializer):
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
        model = SellerList
        fields = (
            "id",
            "property_detail",
            "apn",
            "client_code",
            "date_lead_added",
            "lead_type",
            "seller_lead_name",
            "phone_number",
            "email",
            "lead_status",
            "seller_asking_price",
            "counter_offer_amount",
            "lead_assigned_to",
            "total_minutes_consumed",
            "notes",
        )


class CounterOfferSerializer(serializers.Serializer):
    class Meta:
        model = CounterOffer
        fields = ("amount",)
