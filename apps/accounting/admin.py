from django.contrib import admin

from apps.accounting.models import Category, Company, InternalAccounting


class InternalAccountingAdmin(admin.ModelAdmin):
    model = InternalAccounting
    list_display = ("month", "date", "company", "category", "amount", "reference")
    list_filter = ("month", "company", "category")
    search_fields = ("company__name", "category__name")


admin.site.register(Category)
admin.site.register(Company)
admin.site.register(InternalAccounting, InternalAccountingAdmin)