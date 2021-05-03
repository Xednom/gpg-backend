from rest_framework import serializers

from apps.authentication.models import Staff
from apps.timesheet.models import StaffAccountBalance


__all__ = ("StaffAccountBalanceSerializer",)


class StaffAccountBalanceSerializer(serializers.ModelSerializer):
    staff = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all(), required=False, allow_null=True)
    amount_due_w_currency = serializers.SerializerMethodField()

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
            "account_balance",
            "notes"
        )

    def get_amount_due_w_currency(self, instance):
        if instance.amount_due:
            return f"{instance.amount_due}"