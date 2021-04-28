from djmoney.models.fields import MoneyField
from django.db import models

from apps.core.models import TimeStamped
from apps.authentication.models import Client, Staff


class Status(models.TextChoices):
    submitted = "submitted", ("Submitted")
    approved = "approved", ("Approved")
    dispute = "dispute", ("Dispute")
    waived = "waived", ("Waived")


class PaymentHistory(TimeStamped):
    client = models.ForeignKey(
        Client, related_name="client_payment_histories", on_delete=models.DO_NOTHING
    )
    date = models.DateField()
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency="USD")
    transaction_number = models.CharField(max_length=250)
    payment_channel = models.CharField(max_length=250)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Payment Histories"

    def __str__(self):
        return f"{self.client}"


class AccountBalance(TimeStamped):
    client = models.ForeignKey(
        Client, related_name="client_account_summaries", on_delete=models.DO_NOTHING
    )
    total_payment_made = MoneyField(
        max_digits=19, decimal_places=2, default_currency="USD"
    )
    total_time_consumed = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True
    )
    amount_due = MoneyField(max_digits=19, decimal_places=2, default_currency="USD")
    account_balance = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="USD",
        default=0.00,
        blank=True,
        null=True,
    )
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Account Balances"

    def __str__(self):
        return f"Account balance of {self.client}"


class AccountCharge(TimeStamped):
    ticket_number = models.CharField(max_length=150, blank=True)
    client = models.ForeignKey(
        Client, related_name="client_account_charges", on_delete=models.DO_NOTHING
    )
    shift_date = models.DateField(blank=True, null=True)
    job_request = models.CharField(max_length=250)
    job_request_description = models.TextField(blank=True)
    total_items = models.CharField(max_length=250, blank=True)
    notes = models.TextField(blank=True)
    total_time = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.CharField(
        max_length=150, choices=Status.choices, default=Status.submitted, blank=True
    )
    staff = models.ForeignKey(
        Staff,
        related_name="staff_account_charges",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    staff_hourly_rate = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="PHP",
        default=0.00,
        blank=True,
        null=True,
    )
    staff_fee = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="PHP",
        default=0.00,
        blank=True,
        null=True,
    )
    staff_other_fee = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="PHP",
        default=0.00,
        blank=True,
        null=True,
    )
    staff_total_due = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="PHP",
        default=0.00,
        blank=True,
        null=True,
    )
    client_hourly_rate = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="USD",
        default=0.00,
        blank=True,
        null=True,
    )
    client_other_fee = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="USD",
        default=0.00,
        blank=True,
        null=True,
    )
    client_total_charge = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="USD",
        default=0.00,
        blank=True,
        null=True,
    )
    client_total_due = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="USD",
        default=0.00,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Account charges of {self.client}"

    def create_ticket_number(self):
        ticket_code = ""
        last_in = AccountCharge.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            ticket_number = "AC000" + str((int(seq) + 1))
            return ticket_number

        if self.id:
            ticket_number = "AC000" + str(self.id)
            return ticket_number

        in_id = last_in.id
        in_int = int(in_id)
        ticket_code = "AC000" + str(int(in_int) + 1)
        return ticket_code

    def compute_staff_fee(self):
        staff_fee = self.total_time * self.staff_hourly_rate
        return staff_fee

    def compute_staff_total_due(self):
        total = self.staff_fee + self.staff_other_fee
        return total

    def compute_client_other_fee(self):
        fee = self.total_time * self.client_hourly_rate
        return fee

    def compute_client_total_charge(self):
        charge = self.total_time * self.client_hourly_rate
        return charge

    def compute_client_total_amount_due(self):
        total_charge = self.client_other_fee + self.client_total_charge
        return total_charge

    def save(self, *args, **kwargs):
        self.ticket_number = self.create_ticket_number()
        self.staff_fee = self.compute_staff_fee()
        self.staff_total_due = self.compute_staff_total_due()
        self.client_other_fee = self.compute_client_other_fee()
        self.client_total_charge = self.compute_client_total_charge()
        self.client_total_due = self.compute_client_total_amount_due()
        super(AccountCharge, self).save(*args, **kwargs)