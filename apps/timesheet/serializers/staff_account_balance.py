from rest_framework import serializers

from apps.authentication.models import Staff
from apps.timesheet.models import StaffAccountBalance


__all__ = ("StaffAccountBalanceSerializer",)


class StaffAccountBalanceSerializer(serializers.ModelSerializer):
    staff = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    payment_made_w_currency = serializers.CharField(source="payment_made")
    amount_due_w_currency = serializers.SerializerMethodField()
    account_balance_w_currency = serializers.CharField(source="account_balance")

    class Meta:
        model = StaffAccountBalance
        fields = (
            "id",
            "staff",
            "date",
            "amount_due",
            "amount_due_currency",
            "amount_due_w_currency",
            "payment_made",
            "payment_made_w_currency",
            "account_balance",
            "account_balance_w_currency",
            "notes",
        )

    def get_amount_due_w_currency(self, instance):
        if instance.amount_due:
            return f"{instance.amount_due}"
