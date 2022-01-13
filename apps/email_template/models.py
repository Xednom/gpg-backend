from django.db import models

from apps.core.models import TimeStamped


class EmailTemplate(TimeStamped):
    date_added = models.DateTimeField()
    email_template_title = models.CharField(max_length=255)
    url_link = models.TextField()
    email_template_description = models.TextField()
    company_category = models.ForeignKey(
        "core.Company", related_name="company_email_templates", on_delete=models.CASCADE
    )
    notes = models.TextField(blank=True)
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.company_category} - {self.email_template_title}"
