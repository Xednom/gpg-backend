from django.contrib import admin

from apps.gpg.models import (
    JobOrderGeneral,
    JobOrderCategory,
    Comment,
    CommentByPropertDetail,
    PropertyDetail,
    PropertyPrice,
    ListingAdDetail,
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
    list_display = ("ticket_number", "client", "apn", "county", "state", "status")
    fieldsets = (
        (
            "Property Information",
            {
                "fields": (
                    "ticket_number",
                    "client",
                    "apn",
                    "county",
                    "state",
                    "status",
                    "size",
                )
            },
        ),
    )


class PropertyPriceAdmin(admin.ModelAdmin):
    model = PropertyPrice
    list_display = ("property_details", "cash_terms", "status")
    fieldsets = (
        (
            "Property price Information",
            {
                "fields": (
                    "property_details",
                    "asking_price",
                    "cash_terms",
                    "finance_terms",
                    "other_terms",
                    "notes",
                    "status",
                )
            },
        ),
    )


class ListingAdDetailAdmin(admin.ModelAdmin):
    model = ListingAdDetail
    list_display = ("category", "ad_details")
    fieldsets = (
        (
            "Property price Information",
            {
                "fields": (
                    "property_details",
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
        "va_assigned",
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
                    "category",
                    "status",
                    "due_date",
                    "date_completed",
                    "total_time_consumed",
                    "completed_url_work",
                    "va_assigned",
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
admin.site.register(PropertyPrice, PropertyPriceAdmin)
admin.site.register(ListingAdDetail, ListingAdDetailAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
