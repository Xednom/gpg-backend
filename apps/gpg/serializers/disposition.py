from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.gpg.models import Disposition, PropertyDetail
from apps.authentication.models import Staff

__all__ = ("DispositionSerializer",)


class DispositionSerializer(WritableNestedModelSerializer):
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
        model = Disposition
        fields = (
            "property_detail",
            "apn",
            "client_code",
            "selling_price",
            "discounted_cash_price",
            "selling_price_minimum",
            "selling_price_maximum",
            "financed_terms",
            "amount_closed_deal",
            "deal_status",
            "assigned_sales_team",
            "notes",
        )
