from django.contrib import admin

from apps.archive.models import ArchiveJobOrder, ArchiveJobOrderApn
from apps.gpg.models import CommentByApn
from apps.account.models import AccountFile


class ArchiveJobOrderProfile(admin.ModelAdmin):
    model = ArchiveJobOrder
    readonly_fields = ["client_email", "staff_email", "client_file"]
    list_display = (
        "ticket_number",
        "client",
        "client_email",
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

    # def get_staffs(self, obj):
    #     return ", ".join([staff.staff_name for staff in obj.va_assigned.all()])

    # get_staffs.short_description = "Staffs"


class ArchiveJobOrderApnProfile(admin.ModelAdmin):
    model = ArchiveJobOrderApn
    list_display = (
        "created_at",
        "ticket_number",
        "client",
        "client_email",
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


admin.site.register(ArchiveJobOrder, ArchiveJobOrderProfile)
admin.site.register(ArchiveJobOrderApn, ArchiveJobOrderApnProfile)
