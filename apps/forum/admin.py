from django.contrib import admin

from apps.forum.models import Thread, Comment, Reply


class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    list_display = ("title", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("title", "content")
    filter_horizontal = ("staff_carbon_copy", "client_carbon_copy")


admin.site.register(Thread, ThreadAdmin)
