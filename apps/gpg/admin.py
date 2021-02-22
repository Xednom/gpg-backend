from django.contrib import admin

from apps.gpg.models import JobOrderGeneral


class JobOrderGeneralAdmin(admin.ModelAdmin):
    model = JobOrderGeneral


admin.site.register(JobOrderGeneral, JobOrderGeneralAdmin)