from django.db import models

from apps.core.models import TimeStamped


__all__ = ("VendorExpense", "CategoryExpense")


class VendorExpense(TimeStamped):
    category_list = models.ForeignKey(
        "operational_cost.CategoryList",
        related_name="category_list_vendor_expenses",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    cost = models.DecimalField(max_digits=19, decimal_places=2)
    vendor = models.ForeignKey(
        "core.Vendor",
        related_name="vendor_expenses",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.category_list} expense({self.cost})"


class CategoryExpense(TimeStamped):
    category_list = models.ForeignKey(
        "operational_cost.CategoryList",
        related_name="category_list_category_expenses",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    cost = models.DecimalField(max_digits=19, decimal_places=2)
    company = models.ForeignKey(
        "core.Company",
        related_name="category_company_category_expenses",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.category_list} expense({self.cost})"
