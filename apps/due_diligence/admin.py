from django.contrib import admin

from .models import PhoneLineExtension


class PhoneLineExtensionAdmin(admin.ModelAdmin):
    model = PhoneLineExtension
    list_display = (
        "user_id",
        "get_staffs",
        "original_extension_owner",
        "code_name",
        "allocation_company",
    )
    search_fields = (
        "user_id",
        "code_name",
        "allocated_extension_staff__user__first_name",
        "allocated_extension_staff__user__last_name",
        "original_extension_owner",
    )
    fieldsets = (
        (
            "Phone Line Extension Information",
            {
                "fields": (
                    "user_id",
                    "allocated_extension_staff",
                    "original_extension_owner",
                    "code_name",
                    "allocation_company",
                )
            },
        ),
    )
    filter_horizontal = ["allocated_extension_staff"]

    def get_staffs(self, obj):
        return ", ".join(
            [staff.staff_name for staff in obj.allocated_extension_staff.all()]
        )

    get_staffs.short_description = "Allocated extension - Staff assigned"


admin.site.register(PhoneLineExtension, PhoneLineExtensionAdmin)
