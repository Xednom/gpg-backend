from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

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
    english_academy = "english_academy", ("English Academy")
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
    designation_category = models.CharField(
        choices=DesignationCategory.choices, blank=True, max_length=30
    )
    company_category = models.CharField(
        choices=CompanyCategory.choices, blank=True, max_length=40
    )
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone",
        "email",
        "designation_category",
        "company_category",
    ]

    @property
    def user_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Client(TimeStamped):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    client_code = models.CharField(max_length=250, blank=True)
    affiliate_partner_code = models.CharField(max_length=250, blank=True)
    affiliate_partner_name = models.CharField(max_length=250, blank=True)
    pin = models.CharField(max_length=5, blank=True)
    lead_information = models.TextField(
        blank=True, help_text="Where did you hear about our company?"
    )
    customer_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.user} - {self.client_code}"

    def create_client_code(self):
        initial_name = self.user.first_name + self.user.last_name
        client_code = ""

        for i in initial_name.upper().split():
            client_code += i[0]

        last_in = Client.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            client_code = client_code + "000" + str(int(seq) + 1)
            return client_code

        if self.id:
            client_code = client_code + "000" + str(self.id)
            return client_code

        in_id = last_in.id
        in_int = int(in_id)

        client_code = client_code + "000" + str(int(in_int) + 1)
        return client_code

    def create_affiliate_partner_code(self):
        code = self.affiliate_partner_name
        partner_code = ""
        for i in code.upper().split():
            partner_code += i[0]
        last_in = Client.objects.all().order_by("id").last()

        if not last_in:
            for i in code.upper().split():
                partner_code += i[0]
            seq = 0
            partner_code = partner_code + "000" + str((int(seq) + 1))
            return partner_code

        if self.id:
            partner_code = partner_code + "000" + str(self.id)
            return partner_code

        in_id = last_in.id
        in_int = int(in_id)

        partner_code = partner_code + "000" + str(int(in_int) + 1)
        return partner_code

    def create_customer_id(self):
        code = self.user.company_category
        customer_code = ""
        for i in code.upper().split():
            customer_code += i[0]
        last_in = Client.objects.all().order_by("id").last()
        if not last_in:
            for i in code.upper().split():
                customer_code += i[0]
            seq = 0
            customer_code = customer_code + "000" + str((int(seq) + 1))
            return customer_code

        if self.id:
            customer_code = customer_code + "000" + str(self.id)
            return customer_code

        in_id = last_in.id
        in_int = int(in_id)

        customer_code = customer_code + "000" + str(int(in_int) + 1)
        return customer_code

    def save(self, *args, **kwargs):
        self.client_code = self.create_client_code()
        self.affiliate_partner_code = self.create_affiliate_partner_code()
        self.customer_id = self.create_customer_id()
        super().save(*args, **kwargs)

    @property
    def client_name(self):
        return f"{self.user.user_full_name}"


class Staff(TimeStamped):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    blood_type = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=250, blank=True)
    company_id = models.CharField(max_length=50, blank=True)
    staff_id = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    company_email = models.EmailField(blank=True)
    start_date_hired = models.DateField(blank=True, null=True)
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
    residential_address = models.TextField(blank=True)
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
        return f"{self.user.user_full_name} - staff"

    @property
    def staff_name(self):
        return f"{self.user.user_full_name}"

    def create_company_id(self):
        code = self.user.company_category
        company_code = ""
        for i in code.upper().split():
            company_code += i[0]
        last_in = Staff.objects.all().order_by("id").last()
        if not last_in:
            seq = 0
            company_code = company_code + "000" + str((int(seq) + 1))
            return company_code

        if self.id:
            company_code = company_code + "000" + str(self.id)
            return company_code

        in_id = last_in.id
        in_int = int(in_id)
        company_code = company_code + "000" + str(int(in_int) + 1)

        return company_code

    def create_staff_id(self):
        initial_name = self.user.user_full_name
        code = self.user.company_category
        staff_code = ""
        staff_initials = ""

        for i in initial_name.upper().split():
            staff_initials += i[0]

        for i in code.upper().split():
            staff_code += i[0]

        last_in = Staff.objects.all().order_by("id").last()
        if not last_in:

            seq = 0
            staff_code = staff_initials + staff_code + "000" + str((int(seq) + 1))
            return staff_code

        if self.id:
            staff_code = staff_initials + staff_code + "000" + str(self.id)
            return staff_code

        in_id = last_in.id
        in_int = int(in_id)
        staff_code = staff_initials + staff_code + "000" + str(int(in_int) + 1)

        return staff_code

    def save(self, *args, **kwargs):
        self.staff_id = self.create_staff_id()
        self.company_id = self.create_company_id()
        super().save(*args, **kwargs)


class InternalFiles(TimeStamped):
    client = models.ForeignKey(
        Client, related_name="client_files", on_delete=models.CASCADE
    )
    file_name = models.CharField(max_length=250, blank=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Internal file"

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
    file_name = models.CharField(max_length=250, blank=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.staff} - {self.file_name}"
