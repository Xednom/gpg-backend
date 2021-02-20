from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.authentication.models import (
    User,
    Client,
    Staff,
    InternalFiles,
    InternalFilesStaff,
)

User = get_user_model()


class InternalFilesAdmin(admin.TabularInline):
    model = InternalFiles
    extra = 1
    readonly_fields = ("created_at",)


class InternalFilesStaffAdmin(admin.TabularInline):
    model = InternalFilesStaff
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


class StaffProfileAdmin(admin.ModelAdmin):
    model = Staff
    list_display = ("user", "staff_id", "company_id")
    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "user",
                    "date_of_birth",
                    "blood_type",
                    "position",
                    "phone_number",
                    "company_email",
                    "start_date_hired",
                    "date_hired_in_contract",
                    "base_pay",
                    "hourly_rate",
                    "status",
                    "category",
                    "residential_address",
                    "company_id",
                    "staff_id",
                )
            },
        ),
        (
            "Government Information",
            {
                "fields": (
                    "tin_number",
                    "sss_number",
                    "pag_ibig_number",
                    "phil_health_number",
                )
            },
        ),
        (
            "Emergency Information",
            {
                "fields": (
                    "emergency_contact_full_name",
                    "relationship",
                    "emergency_contact_number",
                    "mothers_full_name",
                    "mothers_maiden_name",
                    "fathers_full_name",
                )
            },
        ),
        (
            "Payroll Information",
            {
                "fields": (
                    "bank_name",
                    "bank_account_name",
                    "bank_type",
                    "bank_account_number",
                )
            },
        ),
    )
    inlines = [InternalFilesStaffAdmin]


admin.site.register(User, UserProfileAdmin)
admin.site.register(Client, ClientProfileAdmin)
admin.site.register(Staff, StaffProfileAdmin)
admin.site.register(InternalFiles)
