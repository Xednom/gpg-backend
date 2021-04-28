from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import AccountCharge


class AccountChargeSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)

    class Meta:
        model = AccountCharge
        fields = (
            "ticket_number",
            "client",
            "shift_date",
            "job_request",
            "total_items",
            "notes",
            "total_time",
            "status",
            "staff",
            "staff_hourly_rate",
            "staff_hourly_rate_currency",
            "staff_fee",
            "staff_fee_currency",
            "staff_other_fee",
            "staff_other_fee_currency",
            "staff_total_due",
            "staff_total_due_currency",
            "client_hourly_rate",
            "client_hourly_rate_currency",
            "client_other_fee",
            "client_other_fee_currency",
            "client_total_charge",
            "client_total_charge_currency",
            "client_total_due",
            "client_total_due_currency"
        )