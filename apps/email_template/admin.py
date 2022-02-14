from django.contrib import admin

from apps.email_template.models import EmailTemplate


class EmailtemplateAdmin(admin.ModelAdmin):
    model = EmailTemplate
    list_display = (
        "id",
        "email_template_title",
        "email_template_description",
        "created_by",
    )
    list_display_links = (
        "id",
        "email_template_title",
        "email_template_description",
        "created_by",
    )
    search_fields = ("email_template_title", "email_template_description", "created_by")
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (
            "Email template data",
            {
                "fields": (
                    "date_added",
                    "email_template_title",
                    "url_link",
                    "email_template_description",
                    "company_category",
                )
            },
        ),
        (
            "Important date",
            {"fields": ("created_at",)},
        ),
    )


admin.site.register(EmailTemplate, EmailtemplateAdmin)
