from django.db import models

from apps.core.models import TimeStamped, LeadType, LeadStatus


__all__ = ("BuyerList",)


class BuyerList(TimeStamped):
    property_detail = models.ForeignKey(
        "gpg.PropertyDetail",
        related_name="property_detail_buyer_lists",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    apn = models.CharField(max_length=250)
    client_code = models.CharField(max_length=250)
    date_lead_added = models.DateField(auto_now_add=True)
    lead_type = models.CharField(max_length=25, choices=LeadType.choices, blank=True)
    buyer_lead_name = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=250, blank=True)
    lead_status = models.CharField(
        max_length=50, choices=LeadStatus.choices, blank=True
    )
    buyer_offer = models.CharField(max_length=250, blank=True)
    counter_offer_amount = models.ManyToManyField(
        "gpg.CounterOffer", related_name="buyer_counter_offers", blank=True
    )
    lead_assigned_to = models.ForeignKey(
        "authentication.Staff",
        on_delete=models.PROTECT,
        related_name="buyer_lead_assigned_to",
        blank=True,
        null=True,
    )
    total_minutes_consumed = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    notes = models.TextField(blank=True)
