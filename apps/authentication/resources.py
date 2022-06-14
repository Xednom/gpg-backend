from import_export import resources
from apps.authentication.models import Client, User


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
