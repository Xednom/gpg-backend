from import_export import resources
from apps.account.models import AccountFile


class AccountFileResource(resources.ModelResource):
    class Meta:
        model = AccountFile
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "file_name",
            "url",
            "file_description",
        )