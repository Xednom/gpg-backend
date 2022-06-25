from django.contrib import admin

from apps.forum.models import Thread, Comment, Reply


class ThreadComment(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("author", "comment")
    readonly_fields = ["author"]


class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    list_display = ("title", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("title", "content")
    filter_horizontal = ("staff_carbon_copy", "client_carbon_copy")
    inlines = [ThreadComment]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.author = request.user
            instance.save()
        formset.save_m2m()


admin.site.register(Thread, ThreadAdmin)
