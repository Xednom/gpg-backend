from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import AccountBalance

__all__ = ("AccountBalanceSerializer",)


class AccountBalanceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)
    class Meta:
        model = AccountBalance
        fields = (
            "client",
            "total_payment_made",
            "total_time_consumed",
            "amount_due",
            "account_balance",
            "notes"
        )