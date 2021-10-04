from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import AccountBalance

__all__ = ("AccountBalanceSerializer",)


class AccountBalanceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)
    client_code = serializers.CharField(source="client.client_code")
    account_charges = serializers.CharField()
    total_payment_made = serializers.CharField()
    account_balance = serializers.CharField()
    account_balance_amount = serializers.SerializerMethodField()
    class Meta:
        model = AccountBalance
        fields = (
            "id",
            "client",
            "client_code",
            "total_payment_made",
            "total_payment_made_currency",
            "total_time_consumed",
            "account_charges",
            "account_charges_currency",
            "account_balance",
            "account_balance_currency",
            "account_balance_amount",
            "notes"
        )
    
    def get_account_balance_amount(self, instance):
        return instance.account_balance.amount