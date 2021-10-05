from django.db import models

from apps.core.models import TimeStamped

from apps.authentication.models import Client, Staff
from apps.gpg.models import County


__all__ = ("DueDiligenceCallOut",)


class DueDiligenceStatus(models.TextChoices):
    complete = "complete", ("Complete")
    pending = "pending", ("Pending")
    on_hold = "on_hold", ("On Hold")
    cancelled = "cancelled", ("Cancelled")
    for_follow_up = "for_follow_up", ("For Follow Up")
    processing = "processing", ("Processing")
    not_applicable = "not_applicable", ("Not Applicable")
    job_order_request = "job_request", ("Job order request")
    tax_data_complete = "tax_data_complete", ("Tax Data- Complete")
    zoning_data_complete = "zoning_data_complete", ("Zoning Data - Complete")
    utilities_data_complete = "utilities_data_complete", ("Utilities Data - Complete")
    tax_zoning_data_complete = "tax_zoning_data_complete", ("Tax/Zoning Data- Complete")
    tax_utlities_data_complete = "tax_utlities_data_complete", (
        "Tax/Utilies Data - Complete "
    )
    zoning_utilities_data_complete = "zoning_utilities_data_complete", (
        "Zoning/Utilities Data- Complete"
    )


class TaxDataStatus(models.TextChoices):
    complete = "complete", ("Complete")
    pending = "pending", ("Pending")
    on_hold = "on_hold", ("On Hold")
    cancelled = "cancelled", ("Cancelled")
    for_follow_up = "for_follow_up", ("For Follow Up")
    processing = "processing", ("Processing")
    not_applicable = "not_applicable", ("Not Applicable")
    job_order_request = "job_request", ("Job order request")
    tax_data_complete = "tax_data_complete", ("Tax Data- Complete")
    zoning_data_complete = "zoning_data_complete", ("Zoning Data - Complete")
    utilities_data_complete = "utilities_data_complete", ("Utilities Data - Complete")
    tax_zoning_data_complete = "tax_zoning_data_complete", ("Tax/Zoning Data- Complete")
    tax_utlities_data_complete = "tax_utlities_data_complete", (
        "Tax/Utilies Data - Complete "
    )
    zoning_utilities_data_complete = "zoning_utilities_data_complete", (
        "Zoning/Utilities Data- Complete"
    )


class ZoningDataStatus(models.TextChoices):
    complete = "complete", ("Complete")
    pending = "pending", ("Pending")
    on_hold = "on_hold", ("On Hold")
    cancelled = "cancelled", ("Cancelled")
    for_follow_up = "for_follow_up", ("For Follow Up")
    processing = "processing", ("Processing")
    not_applicable = "not_applicable", ("Not Applicable")
    job_order_request = "job_request", ("Job order request")
    tax_data_complete = "tax_data_complete", ("Tax Data- Complete")
    zoning_data_complete = "zoning_data_complete", ("Zoning Data - Complete")
    utilities_data_complete = "utilities_data_complete", ("Utilities Data - Complete")
    tax_zoning_data_complete = "tax_zoning_data_complete", ("Tax/Zoning Data- Complete")
    tax_utlities_data_complete = "tax_utlities_data_complete", (
        "Tax/Utilies Data - Complete "
    )
    zoning_utilities_data_complete = "zoning_utilities_data_complete", (
        "Zoning/Utilities Data- Complete"
    )


class UtilitiesDataStatus(models.TextChoices):
    complete = "complete", ("Complete")
    pending = "pending", ("Pending")
    on_hold = "on_hold", ("On Hold")
    cancelled = "cancelled", ("Cancelled")
    for_follow_up = "for_follow_up", ("For Follow Up")
    processing = "processing", ("Processing")
    not_applicable = "not_applicable", ("Not Applicable")
    job_order_request = "job_request", ("Job order request")
    tax_data_complete = "tax_data_complete", ("Tax Data- Complete")
    zoning_data_complete = "zoning_data_complete", ("Zoning Data - Complete")
    utilities_data_complete = "utilities_data_complete", ("Utilities Data - Complete")
    tax_zoning_data_complete = "tax_zoning_data_complete", ("Tax/Zoning Data- Complete")
    tax_utlities_data_complete = "tax_utlities_data_complete", (
        "Tax/Utilies Data - Complete "
    )
    zoning_utilities_data_complete = "zoning_utilities_data_complete", (
        "Zoning/Utilities Data- Complete"
    )


class QualityReviewStatus(models.TextChoices):
    assinged = "assigned", ("Assigned")
    complete = "complete", ("Complete")
    in_progress = "in_progress", ("In Progress")
    for_verification = "for_verification", ("For Verification")
    pending = "pending", ("Pending")
    on_hold = "on_hold", ("On Hold")
    cancelled = "cancelled", ("Cancelled")
    for_qa_review = "for_qa_review", ("For QA review")


class DueDiligenceCallOut(TimeStamped):
    ticket_number = models.CharField(max_length=250, blank=True)
    client = models.ForeignKey(
        "authentication.Client",
        related_name="call_out_clients",
        on_delete=models.DO_NOTHING,
    )
    dd_link = models.CharField(max_length=500, blank=True)
    assessor_website = models.TextField(
        blank=True, help_text="For Assessed Value & Market Value of the property"
    )
    assessor_contact = models.TextField(
        blank=True, help_text="For Assessed Value & Market Value of the property"
    )
    treasurer_website = models.TextField(
        blank=True, help_text="For Tax Data Collection"
    )
    treasurer_contact = models.TextField(
        blank=True, help_text="For Tax Data Collection"
    )
    recorder_clerk_website = models.TextField(
        blank=True, help_text="For Covenance , Restriction & Deeds"
    )
    recorder_clerk_contact = models.TextField(
        blank=True, help_text="For Covenance , Restriction & Deeds"
    )
    zoning_or_planning_department_website = models.TextField(
        blank=True, help_text="For Zoning Data Collection"
    )
    zoning_or_planning_department_contact = models.TextField(
        blank=True, help_text="For Zoning Data Collection"
    )
    county_environmental_health_department_website = models.TextField(
        blank=True, help_text="For Utilities - Septic, Sewer and Water Data Collection"
    )
    county_environmental_health_department_contact = models.TextField(
        blank=True, help_text="For Utilities - Septic, Sewer and Water Data Collection"
    )
    gis_website = models.TextField(blank=True, help_text="For property map viewing")
    cad_website = models.TextField(blank=True, help_text="For property map viewing")
    electricity_company_name_and_phone_number = models.TextField(
        blank=True, help_text="For Utilities - Electricity Data Collection"
    )
    water_company_name_and_phone_number = models.TextField(
        blank=True, help_text="For Utilities - Septic, Sewer and Water Data Collection"
    )
    sewer_company_name_and_phone_number = models.TextField(
        blank=True, help_text="For Utilities - Septic, Sewer and Water Data Collection"
    )
    gas_company_name_and_phone_number = models.TextField(
        blank=True, help_text="For Utilities - Septic, Sewer and Water Data Collection"
    )
    waste_company_name_and_phone_number = models.TextField(
        blank=True, help_text="For Utilities - Septic, Sewer and Water Data Collection"
    )
    apn = models.CharField(max_length=250)
    county = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    memo_call_notes = models.TextField(blank=True)
    dd_specialists_additional_info = models.TextField(blank=True)
    staff_initial_dd = models.ManyToManyField(
        "authentication.Staff", related_name="staff_initial_due_diligences"
    )
    initial_due_diligence_status = models.CharField(
        max_length=250, choices=DueDiligenceStatus.choices
    )
    initial_dd_quality_review_status = models.CharField(
        max_length=250,
        choices=QualityReviewStatus.choices,
        default=QualityReviewStatus.assinged,
        blank=True,
    )
    initial_dd_date_complete = models.DateField(blank=True, null=True)
    staff_assigned_for_call_out = models.ManyToManyField(
        "authentication.Staff", related_name="staff_assigned_call_out_due_diligences"
    )
    call_out_status = models.CharField(
        max_length=250, choices=DueDiligenceStatus.choices
    )
    tax_data_status = models.CharField(
        max_length=250,
        choices=TaxDataStatus.choices,
        default=TaxDataStatus.processing,
        blank=True,
    )
    zoning_data_status = models.CharField(
        max_length=250,
        choices=ZoningDataStatus.choices,
        default=ZoningDataStatus.processing,
        blank=True,
    )
    utilities_data_status = models.CharField(
        max_length=250,
        choices=UtilitiesDataStatus.choices,
        default=UtilitiesDataStatus.processing,
        blank=True,
    )
    call_out_dd_quality_review_status = models.CharField(
        max_length=250,
        choices=QualityReviewStatus.choices,
        default=QualityReviewStatus.assinged,
        blank=True,
    )
    call_out_dd_date_complete = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["-ticket_number"]

    def __str__(self):
        return f"Due diligence call out for {self.client}"
