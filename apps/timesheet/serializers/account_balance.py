from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import AccountBalance

__all__ = ("AccountBalanceSerializer",)


class AccountBalanceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)
    total_payment_made = serializers.CharField()
    amount_due = serializers.CharField()
    account_balance = serializers.CharField()
    class Meta:
        model = AccountBalance
        fields = (
            "id",
            "client",
            "total_payment_made",
            "total_payment_made_currency",
            "total_time_consumed",
            "amount_due",
            "amount_due_currency",
            "account_balance",
            "account_balance_currency",
            "notes"
        )