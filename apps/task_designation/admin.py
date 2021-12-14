from django.contrib import admin

from apps.task_designation.models import TaskDesignation, AssignmentNote


class AssignmentNoteInline(admin.TabularInline):
    model = AssignmentNote
    extra = 1
    readonly_fields = ('created_at', 'updated_at')


class TaskDesignationAdmin(admin.ModelAdmin):
    model = TaskDesignation
    list_display = ("date", "staff", "client", "managers_note")
    list_filter = ("date", "staff", "client")
    search_fields = (
        "staff__user__first_name",
        "staff__user__last_name",
        "client__user__first_name",
        "client__user__last_name",
    )
    fieldsets = (
        (
            "Task designation details",
            {
                "fields": (
                    "date",
                    "staff",
                    "client",
                )
            },
        ),
        (
            "Other details",
            {
                "fields": (
                    "managers_note",
                )
            },
        ),
    )
    inlines = [AssignmentNoteInline]


admin.site.register(TaskDesignation, TaskDesignationAdmin)
admin.site.register(AssignmentNote)