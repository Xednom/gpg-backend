from django.contrib import admin

from apps.core.admin import ModelAdminMixin
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
    County,
    PropertyDetailFile,
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
    search_fields = ("category",)


class DeadlineAdmin(admin.ModelAdmin):
    model = Deadline
    list_display = ("deadline",)
    search_fields = ("deadline",)


class PropertyPriceAdmin(admin.TabularInline):
    model = PropertyPrice
    extra = 1


class PropertyDetailFileAdmin(admin.TabularInline):
    model = PropertyDetailFile
    extra = 1


class PropertyDetailsAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = PropertyDetail
    list_display = ("apn", "client", "get_staffs", "county", "state", "property_status", "size")
    list_filter = ("client", "county", "state", "property_status")
    search_fields = ("apn", "client__client_code", "county", "state")
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
    filter_horizontal = ("staff",)
    inlines = [PropertyPriceAdmin, PropertyDetailFileAdmin]

    def get_client(self, obj):
        if self.request.user.is_superuser:
            if obj.client:
                return (
                    obj.client.user.first_name
                    + " "
                    + obj.client.user.last_name
                    + " - "
                    + obj.client.client_code
                )
        else:
            return obj.client.client_code or obj.client.user
    
    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.staff.all()])

    get_staffs.short_description = "Staffs"


class PropertyPriceAdmin(admin.ModelAdmin):
    model = PropertyPrice
    list_display = (
        "property_detail",
        "user",
        "asking_price",
        "cash_terms",
        "finance_terms",
        "price_status",
    )
    list_filter = ("asking_price",)
    search_fields = ("property_detail",)
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
        ("Important information", {"fields": ("updated_info",)}),
    )


class PropertyDetailFileAdmin(admin.ModelAdmin):
    model = PropertyDetailFile
    list_display = ("property_detail", "details")
    search_fields = ("property_detail__apn", "details")


class JobOrderGeneralAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = JobOrderGeneral
    readonly_fields = ["client_email", "staff_email"]
    list_display = (
        "ticket_number",
        "client",
        "get_staffs",
        "request_date",
        "due_date",
        "job_title",
        "date_completed",
        "total_time_consumed",
        "status",
    )
    search_fields = (
        "ticket_number",
        "client__user__first_name",
        "client__user__last_name",
        "job_title",
    )
    filter_horizontal = ("va_assigned",)
    list_filter = ("client", "job_title", "status")
    inlines = [JobOrderComment]

    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.va_assigned.all()])

    get_staffs.short_description = "Staffs"


class JobOrderByCategoryAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = JobOrderCategory
    list_display = (
        "ticket_number",
        "client",
        "get_staffs",
        "category",
        "deadline",
        "property_detail",
        "total_time_consumed",
        "due_date",
        "date_completed",
        "status",
    )
    list_filter = (
        "client",
        "staff",
        "category__category",
        "status",
        "total_time_consumed",
    )
    search_fields = (
        "property_detail__apn",
        "ticket_number",
        "client__user__username",
        "client__user__first_name",
        "client__user__last_name",
    )
    readonly_fields = ["client_email", "staff_email"]
    filter_horizontal = ("staff",)
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
                    "deadline",
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

    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.staff.all()])

    get_staffs.short_description = "Staffs"


class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = ("name",)
    search_fields = ("name",)


class CountyAdmin(admin.ModelAdmin):
    model = County
    list_display = ("name", "state")
    search_fields = ("name", "state__name")


admin.site.register(JobOrderGeneral, JobOrderGeneralAdmin)
admin.site.register(JobOrderCategory, JobOrderByCategoryAdmin)
admin.site.register(PropertyDetail, PropertyDetailsAdmin)
admin.site.register(PropertyPrice, PropertyPriceAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
admin.site.register(Deadline, DeadlineAdmin)
admin.site.register(PropertyDetailFile, PropertyDetailFileAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)
