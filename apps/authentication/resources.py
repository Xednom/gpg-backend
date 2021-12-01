from import_export import resources
from apps.authentication.models import Client


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
