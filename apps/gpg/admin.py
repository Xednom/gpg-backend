from django.contrib import admin

from apps.gpg.models import (
    JobOrderGeneral,
    JobOrderCategory,
    Comment,
    Deadline,
    CommentByApn,
    PropertyDetail,
    PropertyPrice,
    CategoryType,
    State,
    County
)


class JobOrderComment(admin.TabularInline):
    model = Comment
    extra = 1


class JobOrderCategoryComment(admin.TabularInline):
    model = CommentByApn
    extra = 1


class CategoryTypeAdmin(admin.ModelAdmin):
    model = CategoryType
    list_display = ("category",)


class DeadlineAdmin(admin.ModelAdmin):
    model = Deadline
    list_display = ("deadline",)


class PropertyPriceAdmin(admin.TabularInline):
    model = PropertyPrice
    extra = 1


class PropertyDetailsAdmin(admin.ModelAdmin):
    model = PropertyDetail
    list_display = ("ticket_number", "client", "apn", "county", "state", "property_status")
    readonly_fields = ["client_email", "staff_email"]
    fieldsets = (
        (
            "Property Information",
            {
                "fields": (
                    "ticket_number",
                    "client",
                    "client_email",
                    "staff",
                    "staff_email",
                    "apn",
                    "county",
                    "state",
                    "property_status",
                    "size",
                )
            },
        ),
        (
            "Listing Ad Detail",
            {
                "fields": (
                    "company_name",
                    "phone",
                    "email",
                    "website_url",
                    "file_storage",
                    "notes_client_side",
                    "notes_va_side",
                    "notes_management_side",
                )
            },
        ),
    )
    inlines = [PropertyPriceAdmin]


class PropertyPriceAdmin(admin.ModelAdmin):
    model = PropertyPrice
    list_display = ("property_detail", "price_status")
    readonly_fields = ["updated_info"]
    fieldsets = (
        (
            "Property price Information",
            {
                "fields": (
                    "property_detail",
                    "price_status",
                    "asking_price",
                    "cash_terms",
                    "finance_terms",
                    "other_terms",
                    "notes",
                )
            },
        ),
        (
            "Important information",
            {
                "fields": (
                    "updated_info",
                )
            }
        ),
    )


class JobOrderGeneralAdmin(admin.ModelAdmin):
    model = JobOrderGeneral
    readonly_fields = ["client_email", "staff_email"]
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
    readonly_fields = ["client_email", "staff_email"]
    inlines = [JobOrderCategoryComment]
    fieldsets = (
        (
            "Job Order by Category Information",
            {
                "fields": (
                    "ticket_number",
                    "property_detail",
                    "client",
                    "client_email",
                    "category",
                    "status",
                    "due_date",
                    "date_completed",
                    "total_time_consumed",
                    "url_of_the_completed_jo",
                    "staff",
                    "staff_email",
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
admin.site.register(CategoryType, CategoryTypeAdmin)
admin.site.register(Deadline, DeadlineAdmin)
admin.site.register(State)
admin.site.register(County)
