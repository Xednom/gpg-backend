from django.contrib import admin

from .models import PhoneLineExtension, DueDiligenceCallOut


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


class DueDiligenceCallOutAdmin(admin.ModelAdmin):
    model = DueDiligenceCallOut
    filter_horizontal = ("staff_initial_dd", "staff_assigned_for_call_out")
    list_display = (
        "ticket_number",
        "client",
        "apn",
        "initial_due_diligence_status",
        "initial_dd_date_complete",
        "call_out_status",
        "call_out_dd_date_complete",
    )

    list_filter = ("initial_due_diligence_status", "call_out_status")
    search_fields = (
        "ticket_number",
        "client__user__first_name",
        "client__user__first_name",
        "apn",
        "county__name",
        "county__state__name",
        "staff_initial_dd__user__first_name",
        "staff_initial_dd__user__last_name",
        "staff_assigned_for_call_out__user__first_name",
        "staff_assigned_for_call_out__user__last_name",
    )
    fieldsets = (
        (
            "Staff assigned and Status for Call outs",
            {
                "fields": (
                    "staff_initial_dd",
                    "initial_due_diligence_status",
                    "initial_dd_date_complete",
                    "staff_assigned_for_call_out",
                    "call_out_status",
                    "call_out_dd_date_complete"
                )
            },
        ),
        (
            "Due diligence call out Information",
            {
                "fields": (
                    "ticket_number",
                    "client",
                    "dd_link",
                    "apn",
                    "county",
                    "state",
                    "memo_call_notes",
                    "dd_specialists_additional_info",
                    "assessor_website",
                    "assessor_contact",
                    "treasurer_website",
                    "treasurer_contact",
                    "recorder_clerk_website",
                    "recorder_clerk_contact",
                    "zoning_or_planning_department_website",
                    "zoning_or_planning_department_contact",
                    "county_environmental_health_department_website",
                    "county_environmental_health_department_contact",
                    "gis_website",
                    "cad_website",
                    "electricity_company_name_and_phone_number",
                    "water_company_name_and_phone_number",
                    "sewer_company_name_and_phone_number",
                    "gas_company_name_and_phone_number",
                    "waste_company_name_and_phone_number",
                )
            },
        )
    )


admin.site.register(PhoneLineExtension, PhoneLineExtensionAdmin)
admin.site.register(DueDiligenceCallOut, DueDiligenceCallOutAdmin)
