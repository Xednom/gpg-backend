from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from apps.core.admin import ModelAdminMixin
from import_export.admin import ImportExportModelAdmin
from apps.timesheet.models import (
    PaymentHistory,
    AccountBalance,
    AccountCharge,
    StaffPaymentHistory,
    StaffAccountBalance,
    PaymentPortal
)
from apps.timesheet.resources import AccountChargeResource


class PaymentHistoryAdmin(admin.ModelAdmin):
    model = PaymentHistory
    list_filter = ("client",)
    list_display = (
        "client",
        "date",
        "amount",
        "transaction_number",
        "payment_channel",
    )


class AccountBalanceAdmin(admin.ModelAdmin):
    model = AccountBalance
    list_filter= ("client",)
    list_display = (
        "client",
        "total_payment_made",
        "total_time_consumed",
        "account_charges",
        "account_balance",
        "get_client_email"
    )

    def get_client_email(self, obj):
        return obj.client.user.email
    
    get_client_email.short_description = "Client email"


def charge_approval(AccountChargeAdmin, request, queryset):
    queryset.update(status="approved")

charge_approval.short_description='Mark selected charges as Approved'


class AccountChargeAdmin(ImportExportModelAdmin):
    model = AccountCharge
    resource_class = AccountChargeResource
    actions = [charge_approval]
    list_display = (
        "ticket_number",
        "shift_date",
        "job_request",
        "job_request_description",
        "status",
        "client",
        "total_time",
        "client_hourly_rate",
        "client_other_fee",
        "client_total_charge",
        "client_total_due",
        "staff",
        "staff_hourly_rate",
        "staff_fee",
        "staff_other_fee",
        "staff_total_due",
    )
    readonly_fields = (
        "client_total_due",
        "client_total_charge",
        "staff_total_due",
    )
    list_filter = ("client", "staff", "status", ("shift_date", DateRangeFilter))
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
    list_filter = ("staff", ("date", DateRangeFilter))
    search_fields = (
        "transaction_number",
        "staff__user__first_name",
        "staff__user__last_name",
    )


class StaffAccountBalanceAdmin(admin.ModelAdmin):
    model = StaffAccountBalance
    list_display = ("date", "staff", "amount_due", "payment_made", "account_balance")
    search_fields = ("staff__user__first_name", "staff__user__last_name")
    list_filter = ("date", "staff")


class PaymentPortalAdmin(admin.ModelAdmin):
    model = PaymentPortal
    list_display = ("name", "url")
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(AccountBalance, AccountBalanceAdmin)
admin.site.register(AccountCharge, AccountChargeAdmin)
admin.site.register(StaffPaymentHistory, StaffPaymentHistoryAdmin)
admin.site.register(StaffAccountBalance, StaffAccountBalanceAdmin)
admin.site.register(PaymentPortal, PaymentPortalAdmin)