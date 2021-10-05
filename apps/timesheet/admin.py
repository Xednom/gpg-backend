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
    PaymentPortal,
)
from apps.timesheet.resources import (
    AccountChargeResource,
    PaymentHistoryResource,
    AccountBalanceResource,
)


class PaymentHistoryAdmin(ImportExportModelAdmin):
    model = PaymentHistory
    resource_class = PaymentHistoryResource
    list_filter = (("date", DateRangeFilter), "client", "payment_channel")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "transaction_number",
    )
    list_display = (
        "client",
        "date",
        "amount",
        "transaction_number",
        "payment_channel",
        "notes",
    )


class AccountBalanceAdmin(ImportExportModelAdmin):
    model = AccountBalance
    resource_class = AccountBalanceResource
    list_filter = ("client",)
    search_fields = ("client__user__first_name", "client__user__last_name", "client__user__username")
    list_display = (
        "client",
        "total_payment_made",
        "total_time_consumed",
        "account_charges",
        "account_balance",
        "get_client_email",
        "billing_status"
    )

    def get_client_email(self, obj):
        return obj.client.user.email

    get_client_email.short_description = "Client email"


def charge_approval(AccountChargeAdmin, request, queryset):
    queryset.update(status="approved")


charge_approval.short_description = "Mark selected charges as Approved"


class AccountChargeAdmin(ImportExportModelAdmin):
    model = AccountCharge
    resource_class = AccountChargeResource
    actions = [charge_approval]
    # excluded = ["client_hourly_rate"]
    admin_list_display = (
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
    normaluser_list_display = (
        "ticket_number",
        "shift_date",
        "job_request",
        "job_request_description",
        "status",
        "client",
        "total_time",
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
    admin_fieldsets = (
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
    normaluser_fieldsets = (
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
                "fields": {
                    "client"
                }
            }
        )
    )

    def get_fieldsets(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fieldsets = self.admin_fieldsets
        else:
            self.fieldsets = self.normaluser_fieldsets

        return super(AccountChargeAdmin, self).get_fieldsets(request, obj, **kwargs)

    def get_list_display(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.list_display = self.admin_list_display
        else:
            self.list_display = self.normaluser_list_display

        return super(AccountChargeAdmin, self).get_list_display(obj, **kwargs)

    def get_export(self, request, queryset=None, *args, **kwargs):
        # For example only export objects with ids in 1, 2, 3 and 4
        if not request.user.is_superuser:
            queryset = queryset and queryset.exclude(
                "client_hourly_rate",
                "client_other_fee",
                "client_total_charge",
                "client_total_due",
            )
            return super(AccountChargeAdmin, self).export(queryset, *args, **kwargs)
        elif request.user.is_superuser:
            queryset = queryset and queryset.all()
            return super(AccountChargeAdmin, self).export(queryset, *args, **kwargs)


class StaffPaymentHistoryAdmin(admin.ModelAdmin):
    model = StaffPaymentHistory
    list_display = (
        "transaction_number",
        "date",
        "staff",
        "amount",
        "payment_channel",
        "notes",
    )
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
