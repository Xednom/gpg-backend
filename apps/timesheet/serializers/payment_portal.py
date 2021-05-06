from rest_framework import serializers

from apps.timesheet.models import PaymentPortal


class PaymentPortalSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentPortal
        fields = (
            "name",
            "url"
        )
