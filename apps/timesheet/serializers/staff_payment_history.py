from rest_framework import serializers

from apps.authentication.models import Staff
from apps.timesheet.models import StaffPaymentHistory


__all__ = ("StaffPaymentHistorySerializer",)


class StaffPaymentHistorySerializer(serializers.ModelSerializer):
    staff = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    amount_w_currency = serializers.SerializerMethodField()

    class Meta:
        model = StaffPaymentHistory
        fields = (
            "id",
            "staff",
            "date",
            "amount",
            "amount_currency",
            "amount_w_currency",
            "transaction_number",
            "payment_channel",
            "notes",
        )

    def get_amount_w_currency(self, instance):
        if instance.amount:
            return f"{instance.amount}"
