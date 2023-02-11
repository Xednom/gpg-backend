from django.db import models

from apps.core.models import TimeStamped, DealStatus


__all__ = ("Acquisition",)


class PossibleOffer(models.TextChoices):
    yes = "yes", ("Yes")
    no = "no", ("No")


class Acquisition(TimeStamped):
    property_detail = models.ForeignKey(
        "gpg.PropertyDetail",
        related_name="property_detail_acquisition",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    apn = models.CharField(max_length=250)
    client_code = models.CharField(max_length=250, blank=True)
    possible_offer = models.CharField(max_length=250, blank=True)
    approved_amount_from_client = models.CharField(
        max_length=25, choices=PossibleOffer.choices, blank=True
    )
    minimum_amount = models.CharField(max_length=250, blank=True)
    maximum_amount = models.CharField(max_length=250, blank=True)
    amount_closed_deal = models.CharField(max_length=250, blank=True)
    deal_status = models.CharField(
        max_length=250, choices=DealStatus.choices, blank=True
    )
    assigned_sales_team = models.ForeignKey(
        "authentication.Staff",
        related_name="assigned_sales_team_acquistion",
        on_delete=models.PROTECT,
    )
    notes = models.TextField(blank=True)
