from django.db import models

from apps.core.models import TimeStamped


__all__ = ("NetIncome",)


class NetIncome(TimeStamped):
    month_year = models.CharField(max_length=15, blank=True)
    debit = models.DecimalField(max_digits=19, decimal_places=2)
    credit = models.DecimalField(max_digits=19, decimal_places=2)
    net_income = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return f"Total net income is {self.net_income}"