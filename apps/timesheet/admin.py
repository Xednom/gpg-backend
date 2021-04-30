from django.contrib import admin

from apps.core.admin import ModelAdminMixin
from apps.timesheet.models import PaymentHistory, AccountBalance, AccountCharge


class PaymentHistoryAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = PaymentHistory
    list_display = (
        "client",
        "date",
        "amount",
        "transaction_number",
        "payment_channel",
    )


class AccountBalanceAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = AccountBalance
    list_display = (
        "client",
        "total_payment_made",
        "total_time_consumed",
        "amount_due",
        "account_balance",
    )


class AccountChargeAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = AccountCharge
    list_display = (
        "ticket_number",
        "shift_date",
        "client",
        "client_hourly_rate",
        "client_other_fee",
        "client_total_charge",
        "client_total_due",
        "job_request",
        "staff",
        "staff_total_due",
        "client_total_due",
    )
    readonly_fields = (
        "client_total_due",
        "client_total_charge",
        "staff_total_due",
    )
    fieldsets = (
        (
            "Account Charge Information",
            {
                "fields": (
                    "ticket_number",
                    "shift_date",
                    "job_request",
                    "job_request_description",
                    "total_items",
                    "total_time",
                    "status",
                    "notes",
                )
            },
        ),
        (
            "Staff information",
            {
                "fields": (
                    "staff",
                    "staff_hourly_rate",
                    "staff_fee",
                    "staff_other_fee",
                    "staff_total_due",
                )
            },
        ),
        (
            "Client information",
            {
                "fields": (
                    "client",
                    "client_hourly_rate",
                    "client_other_fee",
                    "client_total_charge",
                    "client_total_due",
                )
            },
        ),
    )


admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(AccountBalance, AccountBalanceAdmin)
admin.site.register(AccountCharge, AccountChargeAdmin)
