from django.contrib import admin
from apps.core.admin import ModelAdminMixin

from .models import LoginCredential


class LoginCredentialAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = LoginCredential
    list_display = ("get_client", "category", "url")
    search_fields = ("client", "category", "username", "staff")

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


admin.site.register(LoginCredential, LoginCredentialAdmin)