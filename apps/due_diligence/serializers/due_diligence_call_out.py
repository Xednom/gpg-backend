from rest_framework import serializers

from apps.due_diligence.models import DueDiligenceCallOut

__all__ = ("CallOutSerializer",)


class CallOutSerializer(serializers.ModelSerializer):
    client_code = serializers.CharField(source="client.client_code", required=False, allow_null=True)
    class Meta:
        model = DueDiligenceCallOut
        fields = (
            "id",
            "ticket_number",
            "client",
            "client_code",
            "dd_link",
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
            "apn",
            "county",
            "state",
            "memo_call_notes",
            "dd_specialists_additional_info",
            "staff_initial_dd",
            "initial_due_diligence_status",
            "initial_dd_date_complete",
            "staff_assigned_for_call_out",
            "call_out_status",
            "call_out_dd_date_complete",
        )
