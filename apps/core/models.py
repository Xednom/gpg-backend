from django.db import models


class LeadType(models.TextChoices):
    sellers = "sellers", ("Sellers")
    buyers = "buyers", ("Buyers")


class LeadStatus(models.TextChoices):
    interested = "interested", ("Interested")
    not_interested = "not_interested", ("Not Interested")
    dead_lead = "dead_lead", ("Dead Lead")
    do_not_call_list = "do_not_call_list", ("Do Not Call List")


class Status(models.TextChoices):
    active = "active", ("Active")
    closed = "closed", ("Closed")
    on_hold = "on_hold", ("On Hold")
    canceled = "canceled", ("Canceled")


class TimeStamped(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(TimeStamped):
    name = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name} - {self.branch}"


class Vendor(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class DealStatus(models.TextChoices):
    pending = "pending", ("Pending")
    sold = "sold", ("Sold")
    on_hold = "on_hold", ("On Hold")
    on_going_negotiation = "on_going_negotiation", ("On going negotiation")
    drop_deal = "drop_deal", ("Drop Deal")


class YesOrNoOrNotApplicable(models.TextChoices):
    yes = "yes", ("Yes")
    no = "no", ("No")
    not_applicable = "not_applicable", ("Not Applicable")


class FileModel(TimeStamped):
    apn = models.CharField(max_length=250)
    client_code = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    description_of_request = models.TextField(blank=True)
    completed_job_order_file = models.TextField(blank=True)
    date_completed = models.DateField(blank=True, null=True)
    status_of_job = models.CharField(max_length=25, choices=Status.choices, blank=True)

    class Meta:
        abstract = True
