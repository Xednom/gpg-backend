from django.contrib import admin

from apps.core.models import Company

# Register your models here.


class ModelAdminMixin:
    def get_queryset(self, request):
        qs = super(ModelAdminMixin, self).get_queryset(request)
        self.request = request
        return qs


admin.site.register(Company)