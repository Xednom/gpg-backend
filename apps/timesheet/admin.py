from django.contrib import admin

from apps.core.admin import ModelAdminMixin
from apps.timesheet.models import (
    PaymentHistory,
    AccountBalance,
    AccountCharge,
    StaffPaymentHistory,
    StaffAccountBalance,
)


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
        "account_charges",
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


class StaffPaymentHistoryAdmin(admin.ModelAdmin):
    model = StaffPaymentHistory
    list_display = ("transaction_number", "date", "staff", "amount", "payment_channel")
    search_fields = (
        "transaction_number",
        "staff__user__first_name",
        "staff__user__last_name",
    )


class StaffAccountBalanceAdmin(admin.ModelAdmin):
    model = StaffAccountBalance
    list_display = ("date", "staff", "amount_due", "payment_made", "account_balance")
    search_fields = ("staff__user__first_name", "staff__user__last_name")
    list_filter = ("date",)


admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(AccountBalance, AccountBalanceAdmin)
admin.site.register(AccountCharge, AccountChargeAdmin)
admin.site.register(StaffPaymentHistory, StaffPaymentHistoryAdmin)
admin.site.register(StaffAccountBalance, StaffAccountBalanceAdmin)
