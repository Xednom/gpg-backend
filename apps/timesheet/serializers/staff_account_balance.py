import datetime

from django.db.models import Sum

from rest_framework import serializers

from apps.authentication.models import Staff
from apps.timesheet.models import (
    StaffAccountBalance,
    StaffPaymentHistory,
    AccountCharge,
)


__all__ = ("StaffAccountBalanceSerializer",)


class StaffAccountBalanceSerializer(serializers.ModelSerializer):
    staff = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    payment_made_w_currency = serializers.CharField(source="payment_made")
    amount_due_w_currency = serializers.SerializerMethodField()
    account_balance_w_currency = serializers.CharField(source="account_balance")
    staff_code = serializers.CharField(source="staff.staff_id")
    account_payable = serializers.SerializerMethodField()
    total_time_of_work = serializers.SerializerMethodField()
    timesheet = serializers.SerializerMethodField()

    class Meta:
        model = StaffAccountBalance
        fields = (
            "id",
            "staff",
            "date",
            "amount_due",
            "amount_due_currency",
            "amount_due_w_currency",
            "payment_made",
            "payment_made_w_currency",
            "account_balance",
            "account_balance_w_currency",
            "notes",
            "staff_code",
            "account_payable",
            "total_time_of_work",
            "timesheet",
        )

    def get_amount_due_w_currency(self, instance):
        if instance.amount_due:
            return f"{instance.amount_due}"

    def get_total_time_of_work(self, instance):
        current_month = instance.created_at.month
        current_year = instance.created_at.year
        staff_total_time = ""
        if instance.staff:
            staff_total_time = AccountCharge.objects.filter(
                staff=instance.staff,
                created_at__month=current_month,
                created_at__year=current_year,
            ).aggregate(total_time=Sum("total_time"))
            if staff_total_time["total_time"] is not None:
                staff_total_time = staff_total_time["total_time"]
                return staff_total_time
            else:
                return " - "

    def get_account_payable(self, instance):
        current_year = instance.created_at.year
        current_month = instance.created_at.month
        account_payable = ""
        if instance.staff:
            staff_charge = AccountCharge.objects.filter(
                staff=instance.staff,
                created_at__month=current_month,
                created_at__year=current_year,
            ).aggregate(total_charge=Sum("staff_total_due"))
            staff_payment_history = StaffPaymentHistory.objects.filter(
                staff=instance.staff
            ).aggregate(total_payment=Sum("amount"))
            account_payable = (
                staff_charge["total_charge"] - staff_payment_history["total_payment"]
            )
            return account_payable
        else:
            return " - "

    def get_timesheet(self, instance):
        if instance.staff:
            staff_charge = AccountCharge.objects.filter(
                staff=instance.staff,
                created_at__month=instance.created_at.month,
                created_at__year=instance.created_at.year,
            ).aggregate(total_charge=Sum("staff_total_due"))
            print(staff_charge["total_charge"])
            return staff_charge["total_charge"]
