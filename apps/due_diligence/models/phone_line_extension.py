from django.db import models

from apps.core.models import TimeStamped
from apps.authentication.models import Staff


__all__ = ("PhoneLineExtension",)


class PhoneLineExtension(TimeStamped):
    user_id = models.CharField(max_length=250)
    allocated_extension_staff = models.ManyToManyField(
        Staff, related_name="allocated_extension_staffs"
    )
    original_extension_owner = models.CharField(max_length=250, blank=True)
    code_name = models.CharField(max_length=250)
    allocation_company = models.CharField(max_length=250)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"User id({self.user_id}) of {self.allocation_company}"
