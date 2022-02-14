from rest_framework import serializers

from apps.authentication.models import Client
from apps.timesheet.models import AccountCharge


class AccountChargeSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="client_code", queryset=Client.objects.all()
    )
    client_code = serializers.CharField(
        source="client.client_code", required=False, allow_null=True
    )
    staff_code = serializers.CharField(
        source="staff.staff_id", required=False, allow_null=True
    )
    staffs_hourly_rate = serializers.CharField(
        source="staff_hourly_rate", required=False, allow_null=True
    )
    staffs_fee = serializers.CharField(
        source="staff_fee", required=False, allow_null=True
    )
    staffs_other_fee = serializers.CharField(
        source="staff_other_fee", required=False, allow_null=True
    )
    staffs_total_due = serializers.CharField(
        source="staff_total_due", required=False, allow_null=True
    )
    clients_hourly_rate = serializers.CharField(
        source="client.hourly_rate", required=False, allow_null=True
    )
    clients_other_fee = serializers.CharField(
        source="client_other_fee", required=False, allow_null=True
    )
    clients_total_charge = serializers.CharField(
        source="client_total_charge", required=False, allow_null=True
    )
    clients_total_due = serializers.CharField(
        source="client_total_due", required=False, allow_null=True
    )

    class Meta:
        model = AccountCharge
        fields = (
            "id",
            "ticket_number",
            "client",
            "client_code",
            "staff_code",
            "shift_date",
            "job_request",
            "job_request_description",
            "total_items",
            "notes",
            "total_time",
            "status",
            "staff",
            "staff_hourly_rate",
            "staffs_hourly_rate",
            "staff_hourly_rate_currency",
            "staff_fee",
            "staffs_fee",
            "staff_fee_currency",
            "staff_other_fee",
            "staffs_other_fee",
            "staff_other_fee_currency",
            "staff_total_due",
            "staffs_total_due",
            "staff_total_due_currency",
            "client_hourly_rate",
            "clients_hourly_rate",
            "client_hourly_rate_currency",
            "client_other_fee",
            "clients_other_fee",
            "client_other_fee_currency",
            "client_total_charge",
            "clients_total_charge",
            "client_total_charge_currency",
            "client_total_due",
            "clients_total_due",
            "client_total_due_currency",
        )
