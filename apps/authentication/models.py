from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import TimeStamped


class DesignationCategory(models.TextChoices):
    staff = "staff", ("Staff")
    new_client = "new_client", ("New Client")
    current_client = "current_client", ("Current Client")
    affiliate_partner = "affiliate_partner", ("Affiliate Partner")


class CompanyCategory(models.TextChoices):
    gpg_corp = "gpg_corporation", ("GPG Corporation")
    land_master = "land_master", ("Landmaster.us")
    call_me = "call_me_ph", ("CallMe.com.ph")
    psalms_global = "psalms_global", ("Psalmsglobal.com")
    affiliate_partner = "affiliate_partner", ("Affiliate Partner")


class StaffStatus(models.TextChoices):
    regular = "regular", ("Regular")
    probitionary = "probitionary", ("Probitionary")
    inactive = "inactive", ("Inactive")


class StaffCategory(models.TextChoices):
    office_based = "office_based", ("Office Based")
    part_timers = "part_timers", ("Part-timers")
    home_based = "home_based", ("Home Based")


class User(AbstractUser):
    phone = models.CharField(blank=True, max_length=50)
    email = models.EmailField(max_length=254)
    designation_category = models.CharField(
        choices=DesignationCategory.choices, blank=True, max_length=30
    )
    company_category = models.CharField(
        choices=CompanyCategory.choices, blank=True, max_length=40
    )
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    @property
    def user_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Client(TimeStamped):
    user = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)
    client_code = models.CharField(max_length=250, blank=True)
    affiliate_partner_code = models.CharField(max_length=250, blank=True)
    affiliate_partner_name = models.CharField(max_length=250, blank=True)
    pin = models.CharField(max_length=5)
    lead_information = models.TextField(
        help_text="Where did you hear about our company?"
    )
    customer_id = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user} - {self.affiliate_partner_name}"

    @property
    def client_name(self):
        return f"{user.first_name} {user.last_name}"


class Staff(TimeStamped):
    user = models.ForeignKey(User, related_name="staffs", on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    blood_type = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=250)
    company_id = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, blank=True)
    company_email = models.EmailField()
    start_date_hired = models.DateField()
    date_hired_in_contract = models.DateField(blank=True, null=True)
    base_pay = models.CharField(max_length=100, blank=True)
    hourly_rate = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=50,
        choices=StaffStatus.choices,
        default=StaffStatus.probitionary,
        blank=True,
    )
    category = models.CharField(
        max_length=50,
        choices=StaffCategory.choices,
        default=StaffCategory.office_based,
        blank=True,
    )
    residential_address = models.TextField()
    tin_number = models.CharField(max_length=250, blank=True)
    sss_number = models.CharField(max_length=250, blank=True)
    pag_ibig_number = models.CharField(max_length=250, blank=True)
    phil_health_number = models.CharField(max_length=250, blank=True)
    emergency_contact_full_name = models.CharField(max_length=250, blank=True)
    relationship = models.CharField(max_length=250, blank=True)
    emergency_contact_number = models.CharField(max_length=250, blank=True)
    mothers_full_name = models.CharField(max_length=250, blank=True)
    mothers_maiden_name = models.CharField(max_length=250, blank=True)
    fathers_full_name = models.CharField(max_length=250, blank=True)
    bank_name = models.CharField(max_length=250, blank=True)
    bank_account_name = models.CharField(max_length=250, blank=True)
    bank_type = models.CharField(max_length=250, blank=True)
    bank_account_number = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{user.user_full_name} - Staff"

class InternalFiles(TimeStamped):
    client = models.ForeignKey(
        Client, related_name="client_files", on_delete=models.CASCADE
    )
    file_name = models.CharField(max_length=250)
    url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} - {self.file_name}"


class InternalFilesStaff(TimeStamped):
    staff = models.ForeignKey(
        Staff,
        related_name="staff_files",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )