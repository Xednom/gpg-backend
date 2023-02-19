from django.db import models

from apps.core.models import TimeStamped, DealStatus


__all__ = ("Disposition",)


class Disposition(TimeStamped):
    property_detail = models.ForeignKey(
        "gpg.PropertyDetail",
        related_name="property_detail_disposition",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    apn = models.CharField(max_length=250)
    client_code = models.CharField(max_length=250)
    selling_price = models.CharField(max_length=250, blank=True)
    discounted_cash_price = models.CharField(max_length=250, blank=True)
    selling_price_minimum = models.CharField(max_length=250, blank=True)
    selling_price_maximum = models.CharField(max_length=250, blank=True)
    financed_terms = models.TextField(blank=True)
    amount_closed_deal = models.CharField(max_length=250, blank=True)
    deal_status = models.CharField(
        max_length=250,
        choices=DealStatus.choices,
        default=DealStatus.pending,
        blank=True,
    )
    assigned_sales_team = models.ForeignKey(
        "authentication.Staff",
        related_name="disposition_staff",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    notes = models.TextField(blank=True)
