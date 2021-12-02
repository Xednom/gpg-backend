from django.db import models

from apps.core.models import TimeStamped


__all__ = ("MonthlyLiability",)


class MonthlyLiability(TimeStamped):
    vendor = models.ForeignKey(
        "core.Vendor", on_delete=models.SET_NULL, blank=True, null=True
    )
    account_name = models.CharField(max_length=255, blank=True)
    account_number = models.CharField(max_length=255, blank=True)
    monthly_cost = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    contract_start = models.DateField()
    contract_end = models.DateField(blank=True, null=True)
    due_date_every = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    company = models.ForeignKey(
        "core.Company", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"Monthly liability of {self.vendor}"
