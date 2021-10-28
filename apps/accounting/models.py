from django.db import models

from apps.core.models import TimeStamped


class Month(models.TextChoices):
    jan = "jan", ("Jan")
    feb = "feb", ("Feb")
    mar = "mar", ("Mar")
    apr = "apr", ("Apr")
    may = "may", ("May")
    jun = "jun", ("Jun")
    jul = "jul", ("Jul")
    aug = "aug", ("Aug")
    sep = "sep", ("Sep")
    oct = "oct", ("Oct")
    nov = "nov", ("Nov")
    dec = "dec", ("Dec")


class Category(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Company(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"


class InternalAccounting(TimeStamped):
    month = models.CharField(max_length=10, choices=Month.choices)
    date = models.DateField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        related_name="internal_account_categories",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    reference = models.TextField()
    company = models.ForeignKey(
        Company,
        related_name="internal_accounting_companies",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]
