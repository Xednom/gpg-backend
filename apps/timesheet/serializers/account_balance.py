from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import AccountBalance

__all__ = ("AccountBalanceSerializer",)


class AccountBalanceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)
    account_charges = serializers.CharField()
    total_payment_made = serializers.CharField()
    account_balance = serializers.CharField()
    class Meta:
        model = AccountBalance
        fields = (
            "id",
            "client",
            "total_payment_made",
            "total_payment_made_currency",
            "total_time_consumed",
            "account_charges",
            "account_charges_currency",
            "account_balance",
            "account_balance_currency",
            "notes"
        )