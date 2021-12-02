from django.contrib import admin

from apps.operational_cost.models import (
    VendorExpense,
    CategoryExpense,
    Type,
    CategoryList,
    AmountReleasedTo,
    Auditor,
    MonthlyLiability,
    NetIncome,
    OperationalCost,
)
from apps.operational_cost.resources import OperationalCostResource

from import_export.admin import ImportExportModelAdmin


class VendorExpenseAdmin(admin.ModelAdmin):
    model = VendorExpense
    list_display = ("vendor", "cost", "category_list")
    list_filter = ("category_list", "vendor")
    search_fields = ("category_list", "vendor")
    fieldsets = (
        (
            "Vendor Expense",
            {
                "fields": (
                    "category_list",
                    "cost",
                    "vendor",
                )
            },
        ),
    )


class CategoryExpenseAdmin(admin.ModelAdmin):
    model = CategoryExpense
    list_display = ("company", "cost", "category_list")
    list_filter = ("category_list", "company")
    search_fields = ("category_list", "company")
    fieldsets = (
        (
            "Category Expense",
            {
                "fields": (
                    "category_list",
                    "cost",
                    "company",
                )
            },
        ),
    )


class TypeAdmin(admin.ModelAdmin):
    model = Type
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    fieldsets = (
        (
            "Category list",
            {"fields": ("name",)},
        ),
    )


class CategoryListAdmin(admin.ModelAdmin):
    model = CategoryList
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    fieldsets = (
        (
            "Category list",
            {"fields": ("name",)},
        ),
    )


class AmountReleasedToAdmin(admin.ModelAdmin):
    model = AmountReleasedTo
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    fieldsets = (
        (
            "Amount released to",
            {"fields": ("name",)},
        ),
    )


class AuditorAdmin(admin.ModelAdmin):
    model = Auditor
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    fieldsets = (
        (
            "Auditor",
            {"fields": ("name",)},
        ),
    )


class MonthlyLiabilityAdmin(admin.ModelAdmin):
    model = MonthlyLiability
    list_display = (
        "vendor",
        "account_name",
        "account_number",
        "monthly_cost",
        "contract_start",
        "contract_end",
        "due_date_every",
    )
    list_filter = ("vendor", "company")
    search_fields = (
        "name",
        "company__name",
        "vendor__name",
        "account_name",
        "account_number",
    )
    fieldsets = (
        (
            "Monthly liability",
            {
                "fields": (
                    "vendor",
                    "company",
                    "account_name",
                    "account_number",
                )
            },
        ),
        (
            "Important info",
            {
                "fields": (
                    "monthly_cost",
                    "contract_start",
                    "contract_end",
                    "due_date_every",
                )
            },
        ),
        ("Other into", {"fields": ("notes",)}),
    )


class NetIncomeAdmin(admin.ModelAdmin):
    model = NetIncome
    list_display = ("debit", "credit", "net_income")
    fieldsets = (
        (
            "Net income",
            {"fields": ("debit", "credit", "net_income")},
        ),
    )


class OperationalCostAdmin(ImportExportModelAdmin):
    model = OperationalCost
    resource_class = OperationalCostResource
    list_display = (
        "month",
        "date",
        "company_name",
        "company_branch",
        "debit",
        "credit",
        "type",
        "category_list",
        "vendors",
        "amount_released_to",
        "auditor_or_released_by",
    )
    list_filter = (
        "vendors",
        "company_name",
        "type",
        "category_list",
        "amount_released_to",
        "auditor_or_released_by",
    )
    search_fields = (
        "month",
        "date",
        "company_name__name",
        "company_branch",
        "amount_released_to__name",
        "auditor_or_released_by__name",
        "vendors__name",
    )
    fieldsets = (
        (
            "Operational Cost",
            {
                "fields": (
                    "company_name",
                    "company_branch",
                    "debit",
                    "credit",
                    "description",
                    "category_list",
                    "vendors",
                    "type",
                )
            },
        ),
        (
            "Important info",
            {
                "fields": (
                    "month",
                    "date",
                    "amount_released_to",
                    "auditor_or_released_by",
                )
            },
        ),
        ("Other into", {"fields": ("notes",)}),
    )


admin.site.register(VendorExpense, VendorExpenseAdmin)
admin.site.register(CategoryExpense, CategoryExpenseAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(AmountReleasedTo, AmountReleasedToAdmin)
admin.site.register(Auditor, AuditorAdmin)
admin.site.register(CategoryList, CategoryListAdmin)
admin.site.register(MonthlyLiability, MonthlyLiabilityAdmin)
admin.site.register(NetIncome, NetIncomeAdmin)
admin.site.register(OperationalCost, OperationalCostAdmin)
