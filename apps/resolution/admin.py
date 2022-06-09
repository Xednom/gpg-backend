from django.contrib import admin

from .models import Resolution, Category, ResolutionComment


class ResolutionCommentSection(admin.TabularInline):
    model = ResolutionComment
    extra = 1
    fields = ("user", "comment",)
    readonly_fields = ("user",)


class ResolutionAdmin(admin.ModelAdmin):
    model = Resolution
    list_display = (
        "date_submitted",
        "description",
        "assigned_to",
        "client",
        "resolution_provided_by_management",
        "status",
        "additional_notes",
    )
    list_filter = ("assigned_to", "client")
    search_fields = (
        "client__username",
        "client__first_name",
        "client__last_name",
        "assigned_to__username",
        "assigned_to__first_name",
        "assigned_to__last_name",
    )
    readonly_fields = ["date_submitted"]
    fieldsets = (
        (
            "Resolution data",
            {
                "fields": (
                    "date_submitted",
                    "category",
                    "status",
                )
            },
        ),
        (
            "Info about the Resolution",
            {
                "fields": (
                    "assigned_to",
                    "client",
                    "description",
                    "resolution_provided_by_management",
                    "additional_notes",
                )
            },
        ),
    )
    inlines = [ResolutionCommentSection]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()


# Register your models here.
admin.site.register(Resolution, ResolutionAdmin)
admin.site.register(Category)
