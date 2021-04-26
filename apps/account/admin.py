from django.contrib import admin
from apps.core.admin import ModelAdminMixin

from .models import LoginCredential, AccountFile


class LoginCredentialAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = LoginCredential
    list_display = ("get_client", "category", "url")
    search_fields = ("client__user__first_name", "client__user__last_name", "category", "username")

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

    def get_client(self, obj):
        if self.request.user.is_superuser:
            return obj.client.client_name, obj.client.client_code
        else:
            return obj.client.client_code

    get_client.admin_order_field = "client__user__first_name"
    get_client.short_description = "Client"


class AccountFileAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = AccountFile
    list_display = ("get_client", "file_name", "url")
    search_fields = ("client", "file_name", "staff")

    def get_client(self, obj):
        if self.request.user.is_superuser:
            return obj.client.client_name, obj.client.client_code
        else:
            return obj.client.client_code

    get_client.admin_order_field = "client__user__first_name"
    get_client.short_description = "Client"


admin.site.register(LoginCredential, LoginCredentialAdmin)
admin.site.register(AccountFile, AccountFileAdmin)