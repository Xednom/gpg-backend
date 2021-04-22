from django.contrib import admin

# Register your models here.


class ModelAdminMixin:
    def get_queryset(self, request):
        qs = super(ModelAdminMixin, self).get_queryset(request)
        self.request = request
        return qs