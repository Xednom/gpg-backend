from django.contrib import admin

from apps.gpg.models import JobOrderGeneral, Comment


class JobOrderComment(admin.TabularInline):
    model = Comment
    extra = 1


class JobOrderGeneralAdmin(admin.ModelAdmin):
    model = JobOrderGeneral
    inlines = [JobOrderComment]


admin.site.register(JobOrderGeneral, JobOrderGeneralAdmin)