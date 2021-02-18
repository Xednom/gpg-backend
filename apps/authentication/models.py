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


class User(AbstractUser):
    phone = models.CharField(blank=True, max_length=50)
    email = models.EmailField(max_length=254)
    designation_category = models.CharField(choices=DesignationCategory.choices, blank=True, max_length=30)
    company_category = models.CharField(choices=CompanyCategory.choices, blank=True, max_length=40)

    @property
    def user_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Client(TimeStamped):
    user = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)
    client_code = models.CharField(max_length=250, blank=True)
    affiliate_partner_code = models.CharField(max_length=250,blank=True)
    affiliate_partner_name = models.CharField(max_length=250, blank=True)
    pin = models.CharField(max_length=5)
    lead_information = models.TextField(help_text="Where did you hear about our company?")
    customer_id = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user} - {self.affiliate_partner_name}"
    
    @property
    def client_name(self):
        return f"{user.first_name} {user.last_name}"


class InternalFiles(TimeStamped):
    client = models.ForeignKey(Client, related_name="client_files", on_delete=models.CASCADE)
    file_name = models.CharField(max_length=250)
    url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} - {self.file_name}"