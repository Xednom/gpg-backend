from django.contrib import admin

from .models import PhoneLineExtension, DueDiligenceCallOut


class PhoneLineExtensionAdmin(admin.ModelAdmin):
    model = PhoneLineExtension
    list_display = (
        "user_id",
        "did",
        "get_staffs",
        "original_extension_owner",
        "code_name",
        "allocation_company",
        "allocation_office"
    )
    search_fields = (
        "user_id",
        "did",
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
                    "did",
                    "allocated_extension_staff",
                    "original_extension_owner",
                    "code_name",
                    "allocation_company",
                    "allocation_office",
                    "login_details",
                    "notes"
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
    change_list_template = "admin/change_list_filter_confirm.html"
    list_display = (
        "ticket_number",
        "client",
        "get_staff_initial_dd",
        "get_staff_assigned_for_call_out",
        "apn",
        "initial_due_diligence_status",
        "initial_dd_quality_review_status",
        "initial_dd_date_complete",
        "call_out_status",
        "call_out_dd_quality_review_status",
        "call_out_dd_date_complete",
        "dd_link",
        "created_at"
    )

    list_filter = (
        "client",
        "staff_initial_dd",
        "initial_due_diligence_status", 
        "initial_dd_quality_review_status",
        "staff_assigned_for_call_out",
        "call_out_status",
        "call_out_dd_quality_review_status"
    )
    search_fields = (
        "ticket_number",
        "client__user__first_name",
        "client__user__last_name",
        "apn",
        "county",
        "staff_initial_dd__user__first_name",
        "staff_initial_dd__user__last_name",
        "staff_assigned_for_call_out__user__first_name",
        "staff_assigned_for_call_out__user__last_name",
    )
    readonly_fields = ("created_at",)
    fieldsets = (
        (
            "Staff assigned and Status for Call outs",
            {
                "fields": (
                    "staff_initial_dd",
                    "initial_due_diligence_status",
                    "initial_dd_quality_review_status",
                    "initial_dd_date_complete",
                    "staff_assigned_for_call_out",
                    "call_out_status",
                    "call_out_dd_quality_review_status",
                    "call_out_dd_date_complete",
                    "created_at",
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

    def get_staff_initial_dd(self, obj):
        return ", ".join(
            [staff.staff_name for staff in obj.staff_initial_dd.all()]
        )
    
    def get_staff_assigned_for_call_out(self, obj):
        return ", ".join(
            [staff.staff_name for staff in obj.staff_assigned_for_call_out.all()]
        )
    
    get_staff_initial_dd.short_description = "Staffs initial Due diligence - assigned"
    get_staff_assigned_for_call_out.short_description = "Staffs assigned for call out"


admin.site.register(PhoneLineExtension, PhoneLineExtensionAdmin)
admin.site.register(DueDiligenceCallOut, DueDiligenceCallOutAdmin)
