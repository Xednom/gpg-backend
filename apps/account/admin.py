from django.contrib import admin
from apps.core.admin import ModelAdminMixin

from .models import LoginCredential, AccountFile

from import_export.admin import ImportExportModelAdmin
from apps.account.resources import AccountFileResource


class LoginCredentialAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = LoginCredential
    list_display = ("client", "get_staffs", "category", "url")
    list_filter = ("client", "staff")
    filter_horizontal = ("staff",)
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "category",
        "username",
    )

    fieldsets = (
        (
            "Login Credentials Information",
            {
                "fields": (
                    "client",
                    "staff",
                    "category",
                    "url",
                    "username",
                    "password",
                    "notes",
                )
            },
        ),
    )

    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.staff.all()])

    get_staffs.short_description = "Staffs"


class AccountFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = AccountFile
    resource_class = AccountFileResource
    list_display = ("client", "get_staffs", "file_name", "url")
    list_filter = ("staff", "client")
    filter_horizontal = ("staff",)
    search_fields = ("client__user__first_name", "client__user__last_name", "file_name")
    fieldsets = (
        (
            "Account file Information",
            {
                "fields": (
                    "client",
                    "staff",
                    "file_name",
                    "url",
                    "file_description",
                )
            },
        ),
    )

    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.staff.all()])

    get_staffs.short_description = "Staffs"


admin.site.register(LoginCredential, LoginCredentialAdmin)
admin.site.register(AccountFile, AccountFileAdmin)
