from import_export import resources
from apps.authentication.models import Client, User, Staff


class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        fields = (
            "user",
            "user__email",
            "client_code",
            "affiliate_partner_code",
            "affiliate_partner_name",
            "pin",
            "lead_information",
            "customer_id",
            "hourly_rate",
        )


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "designation_category",
            "company_category",
        )


class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff
        fields = (
            "user__username",
            "date_of_birth",
            "blood_type",
            "position",
            "company_id",
            "staff_id",
            "phone_number",
            "company_email",
            "start_date_hired",
            "date_hired_in_contract",
            "base_pay",
            "hourly_rate",
            "status",
            "category",
            "residential_address",
            "tin_number",
            "sss_number",
            "pag_ibig_number",
            "phil_health_number",
            "emergency_contact_full_name",
            "relationship",
            "emergency_contact_number",
            "mothers_full_name",
            "mothers_maiden_name",
            "fathers_full_name",
            "bank_name",
            "bank_account_name",
            "bank_type",
            "bank_account_number",
        )
