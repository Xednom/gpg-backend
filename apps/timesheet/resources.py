from django.db import models
from import_export import resources
from apps.timesheet.models import AccountCharge, PaymentHistory


class AccountChargeResource(resources.ModelResource):
    
    class Meta:
        model = AccountCharge
        fields = (
            "ticket_number",
            "shift_date",
            "job_request",
            "job_request_description",
            "total_items",
            "notes",
            "total_time",
            "status",
            "staff__user__first_name",
            "staff__user__last_name",
            "staff_hourly_rate",
            "staff_fee",
            "staff_other_fee",
            "staff_total_due",
            "client__user__first_name",
            "client__user__last_name",
            "client_hourly_rate",
            "client_other_fee",
            "client_total_charge",
            "client_total_due"
        )


class PaymentHistoryResource(resources.ModelResource):

    class Meta:
        model = PaymentHistory
        fields = (
            "date",
            "client__user",
            "amount",
            "transaction_number",
            "payment_channel",
            "notes"
        )