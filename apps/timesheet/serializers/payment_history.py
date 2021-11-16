from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import PaymentHistory


class PaymentHistorySerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="client_code",
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )
    payment_amount = serializers.SerializerMethodField()

    class Meta:
        model = PaymentHistory
        fields = (
            "id",
            "payment_id",
            "client",
            "client_name",
            "date",
            "amount",
            "amount_currency",
            "payment_amount",
            "transaction_number",
            "payment_channel",
            "notes",
        )

    def get_payment_amount(self, instance):
        if instance.amount:
            return f"{instance.amount}"
