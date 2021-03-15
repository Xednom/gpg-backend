from django.contrib import admin

from apps.gpg.models import (
    JobOrderGeneral,
    JobOrderCategory,
    Comment,
    CommentByApn,
    PropertyDetail,
    CategoryType
)


class JobOrderComment(admin.TabularInline):
    model = Comment
    extra = 1


class CategoryTypeAdmin(admin.ModelAdmin):
    model = CategoryType
    list_display = ("category",)


class PropertyDetailsAdmin(admin.ModelAdmin):
    model = PropertyDetail
    list_display = ("ticket_number", "client", "apn", "county", "state", "property_status")
    fieldsets = (
        (
            "Property Information",
            {
                "fields": (
                    "ticket_number",
                    "client",
                    "staff",
                    "apn",
                    "county",
                    "state",
                    "property_status",
                    "size",
                )
            },
        ),
        (
            "Property price Information",
            {
                "fields": (
                    "asking_price",
                    "cash_terms",
                    "finance_terms",
                    "other_terms",
                    "notes",
                    "price_status",
                )
            },
        ),
        (
            "Listing Ad Detail",
            {
                "fields": (
                    "category",
                    "ad_details",
                    "notes_client_side",
                    "notes_va_side",
                    "notes_management_side",
                )
            },
        ),
    )


class JobOrderGeneralAdmin(admin.ModelAdmin):
    model = JobOrderGeneral
    list_display = (
        "ticket_number",
        "client",
        "va_assigned",
        "request_date",
        "due_date",
        "job_title",
        "status",
    )
    inlines = [JobOrderComment]


class JobOrderByCategoryAdmin(admin.ModelAdmin):
    model = JobOrderCategory
    list_display = (
        "ticket_number",
        "client",
        "staff",
        "due_date",
        "date_completed",
        "status",
    )
    fieldsets = (
        (
            "Job Order by Category Information",
            {
                "fields": (
                    "ticket_number",
                    "client",
                    "category",
                    "status",
                    "due_date",
                    "date_completed",
                    "total_time_consumed",
                    "completed_url_work",
                    "staff",
                    "job_description",
                )
            },
        ),
        (
            "Note information",
            {
                "fields": (
                    "notes_va",
                    "notes_management",
                )
            },
        ),
    )


admin.site.register(JobOrderGeneral, JobOrderGeneralAdmin)
admin.site.register(JobOrderCategory, JobOrderByCategoryAdmin)
admin.site.register(PropertyDetail, PropertyDetailsAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
