from django.db import models


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
