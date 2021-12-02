from django.db import models

from apps.core.models import TimeStamped
from django.contrib.auth import get_user_model


User = get_user_model()


__all__ = ("Type", "CategoryList", "AmountReleasedTo", "Auditor", "OperationalCost")


class Type(TimeStamped):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CategoryList(TimeStamped):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AmountReleasedTo(TimeStamped):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Auditor(TimeStamped):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OperationalCost(TimeStamped):
    company_name = models.ForeignKey(
        "core.Company",
        related_name="company_operating_costs",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    company_branch = models.CharField(max_length=255, blank=True)
    month = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    debit = models.DecimalField(max_digits=20, decimal_places=2)
    credit = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category_list = models.ForeignKey(CategoryList, on_delete=models.CASCADE)
    vendors = models.ForeignKey(
        "core.Vendor",
        related_name="vendor_operating_costs",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    notes = models.TextField(blank=True)
    amount_released_to = models.ForeignKey(
        AmountReleasedTo,
        related_name="amount_released_to_operating_costs",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    auditor_or_released_by = models.ForeignKey(
        Auditor,
        related_name="operating_cost_auditors",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Operational Cost of {self.company_name}"

    def save(self, *args, **kwargs):
        if self.company_name:
            self.company_branch = self.company_name.branch
        super(OperationalCost, self).save(*args, **kwargs)
