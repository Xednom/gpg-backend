from django.contrib import admin

from apps.core.admin import ModelAdminMixin
from apps.timesheet.models import PaymentHistory, AccountBalance, AccountCharge


class PaymentHistoryAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = PaymentHistory
    list_display = (
        "get_client",
        "date",
        "amount",
        "transaction_number",
        "payment_channel",
    )

    def get_client(self, obj):
        if self.request.user.is_superuser:
            return obj.client.client_name, obj.client.client_code
        else:
            return obj.client.client_code

    get_client.admin_order_field = "client__user__first_name"
    get_client.short_description = "Client"


class AccountBalanceAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = AccountBalance
    list_display = (
        "get_client",
        "total_payment_made",
        "total_time_consumed",
        "amount_due",
        "account_balance",
    )

    def get_client(self, obj):
        if self.request.user.is_superuser:
            return obj.client.client_name, obj.client.client_code
        else:
            return obj.client.client_code

    get_client.admin_order_field = "client__user__first_name"
    get_client.short_description = "Client"


class AccountChargeAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = AccountCharge
    list_display = (
        "ticket_number",
        "shift_date",
        "get_client",
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
        "client_other_fee",
        "client_total_charge",
        "staff_total_due",
        "staff_fee",
    )

    def get_client(self, obj):
        if self.request.user.is_superuser:
            return obj.client.client_name + " - " + obj.client.client_code
        else:
            return obj.client.client_code

    get_client.admin_order_field = "client__user__first_name"
    get_client.short_description = "Client"


admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(AccountBalance, AccountBalanceAdmin)
admin.site.register(AccountCharge, AccountChargeAdmin)
