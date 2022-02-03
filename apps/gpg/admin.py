from django.contrib import admin

from apps.core.admin import ModelAdminMixin
from apps.account.models import AccountFile
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
    JobOrderCategoryAnalytics,
    JobOrderGeneralAnalytics,
    JobOrderGeneralRating,
    JobOrderCategoryRating,
    JobOrderCategoryAgentScoring,
    JobOrderGeneralAgentScoring
)


class AccountFileInline(admin.TabularInline):
    model = AccountFile
    extra = 1
    fields = ("client", "file_name", "url", "file_description", "staff")
    readonly_fields = ("created_at", "updated_at")


class JobOrderCategoryInline(admin.TabularInline):
    model = JobOrderCategory
    extra = 1
    fields = ("staff",)
    readonly_fields = ("client", "created_at", "updated_at")


class JobOrderComment(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("user", "comment", "created_at", "updated_at")
    readonly_fields = ("user", "created_at", "updated_at")


class JobOrderCategoryComment(admin.TabularInline):
    model = CommentByApn
    extra = 1
    fields = ("user", "comment", "created_at", "updated_at")
    readonly_fields = ("user", "created_at", "updated_at")


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
    list_display = (
        "apn",
        "client",
        "get_staffs",
        "county",
        "state",
        "property_status",
        "size",
    )
    list_filter = ("client", "staff", "county", "state", "property_status")
    search_fields = ("apn", "client__client_code", "county", "state", "property_owner")
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
                    "property_owner",
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


def status_complete(JobOrderGeneralAdmin, request, queryset):
    queryset.update(status="closed")


status_complete.short_description = "Mark selected Job Orders as Closed"


class JobOrderGeneralAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = JobOrderGeneral
    actions = [status_complete]
    readonly_fields = ["client_email", "staff_email", "client_file"]
    list_display = (
        "ticket_number",
        "client",
        "client_email",
        "get_staffs",
        "staff_email",
        "request_date",
        "due_date",
        "job_title",
        "date_completed",
        "total_time_consumed",
        "status",
        "url_of_the_completed_jo",
    )
    search_fields = (
        "ticket_number",
        "client__user__first_name",
        "client__user__last_name",
        "job_title",
    )
    filter_horizontal = ("va_assigned",)
    list_filter = ("client", "va_assigned", "job_title", "status")
    inlines = [JobOrderComment, AccountFileInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.va_assigned.all()])

    get_staffs.short_description = "Staffs"


class JobOrderByCategoryAdmin(ModelAdminMixin, admin.ModelAdmin):
    model = JobOrderCategory
    list_display = (
        "created_at",
        "ticket_number",
        "client",
        "client_email",
        "get_staffs",
        "staff_email",
        "category",
        "deadline",
        "property_detail",
        "total_time_consumed",
        "due_date",
        "date_completed",
        "status",
        "url_of_the_completed_jo",
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
    readonly_fields = ["client_email", "staff_email", "client_file"]
    filter_horizontal = ("staff",)
    inlines = [JobOrderCategoryComment, AccountFileInline]
    fieldsets = (
        (
            "Job Order by Category Information",
            {
                "fields": (
                    "ticket_number",
                    "property_detail",
                    "client",
                    "client_file",
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

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

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


class JobOrderGeneralRatingAdmin(admin.ModelAdmin):
    model = JobOrderGeneralRating
    list_display = (
        "job_order",
        "client",
        "rating",
    )
    list_filter = ("job_order", "client")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "job_order__ticket_number",
        "job_order__job_title",
    )
    readonly_fields = ["job_order", "client", "rating", "comment"]
    fieldsets = (
        (
            "Job order general rate",
            {
                "fields": (
                    "job_order",
                    "client",
                    "rating",
                    "comment",
                )
            },
        ),
    )


class JobOrderCategoryRatingAdmin(admin.ModelAdmin):
    model = JobOrderCategoryRating
    list_display = (
        "job_order",
        "client",
        "rating",
    )
    list_filter = ("job_order", "client")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "job_order__ticket_number",
        "job_order__job_title",
    )
    readonly_fields = ["job_order", "client", "rating", "comment"]
    fieldsets = (
        (
            "Job order general rate",
            {
                "fields": (
                    "job_order",
                    "client",
                    "rating",
                    "comment",
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
admin.site.register(PropertyDetailFile, PropertyDetailFileAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(JobOrderCategoryAnalytics)
admin.site.register(JobOrderGeneralAnalytics)
admin.site.register(JobOrderGeneralRating, JobOrderGeneralRatingAdmin)
admin.site.register(JobOrderCategoryRating, JobOrderCategoryRatingAdmin)
admin.site.register(JobOrderGeneralAgentScoring)
admin.site.register(JobOrderCategoryAgentScoring)