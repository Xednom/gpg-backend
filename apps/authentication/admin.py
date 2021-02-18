from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.authentication.models import User, Client, InternalFiles

User = get_user_model()


class InternalFilesAdmin(admin.TabularInline):
    model = InternalFiles
    extra = 1
    readonly_fields = ("created_at",)


class UserProfileAdmin(UserAdmin):
    UserAdmin.fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal Informations"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "designation_category",
                    "company_category",
                )
            },
        ),
        (
            ("Permissions"),
            {"fields": ("is_active", "is_superuser", "groups", "user_permissions")},
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class ClientProfileAdmin(admin.ModelAdmin):
    model = Client
    list_display = ("user", "affiliate_partner_code", "customer_id")
    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "user",
                    "affiliate_partner_code",
                    "affiliate_partner_name",
                    "pin",
                    "lead_information",
                    "customer_id",
                )
            },
        ),
    )
    inlines = [InternalFilesAdmin]


admin.site.register(User, UserProfileAdmin)
admin.site.register(Client, ClientProfileAdmin)
admin.site.register(InternalFiles)
