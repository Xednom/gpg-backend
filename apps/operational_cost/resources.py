from import_export import resources
from apps.operational_cost.models import OperationalCost


class OperationalCostResource(resources.ModelResource):
    class Meta:
        model = OperationalCost
        fields = (
            "company_name__name",
            "company_branch",
            "month",
            "date",
            "description",
            "debit",
            "credit",
            "type__name",
            "category_list__name",
            "vendors__name",
            "notes",
            "amount_released_to__name",
            "auditor_or_released_by__name",
        )
