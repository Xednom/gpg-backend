from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import PaymentHistory


class PaymentHistorySerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)

    class Meta:
        model = PaymentHistory
        fields = (
            "client",
            "date",
            "amount",
            "amount_currency",
            "transaction_number",
            "payment_channel",
            "notes"
        )