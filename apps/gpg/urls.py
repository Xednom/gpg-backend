from django.urls import include, path
from rest_framework import routers

from apps.authentication.views import (
    StaffViewSet,
    ClientViewSet,
    ClientFilesViewSet,
    StaffFilesViewSet,
    ClientCodeViewSet,
    StaffCodeViewSet
)
from apps.account.views import LoginCredentialViewSet, AccountFileViewSet
from apps.timesheet.views import (
    AccountBalanceViewSet,
    AccountChargeViewSet,
    PaymentHistoryViewSet,
    StaffAccountBalanceViewSet,
    StaffPaymentHistoryViewSet,
    PaymentPortalViewSet
)
from apps.due_diligence.views import PhoneLineExtViewSet, CallOutViewSet

from apps.newsfeed.views import NewsFeedViewSet, CreateNewsFeedComment

from . import views

router = routers.DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff-list")
router.register(r"client", ClientViewSet, basename="client-list")
router.register(r"client-code", ClientCodeViewSet, basename="client-code-list")
router.register(r"staff-code", StaffCodeViewSet, basename="staff-code-list")
router.register(r"client-files", ClientFilesViewSet, basename="client-files-list")
router.register(r"staff-files", StaffFilesViewSet, basename="staff-files-list")
router.register(
    r"job-order", views.JobOrderGeneralViewSet, basename="job-order-general"
)
router.register(
    r"job-order-by-category",
    views.JobOrderByCategoryViewSet,
    basename="job-order-category",
)
router.register(
    r"job-order-by-category-analytics",
    views.JobOrderApnAnalyticsViewSet,
    basename="job-order-category-analytics",
)
router.register(
    r"property-detail", views.PropertyDetailsViewSet, basename="property-details"
)
router.register(
    r"property-price", views.PropertyPriceStatusViewSet, basename="property-prices"
)
router.register(
    r"property-detail-file",
    views.PropertyDetailFileViewSet,
    basename="property-detail-files",
)
router.register(
    r"apn-category-type", views.ApnCategoryViewSet, basename="apn-category-types"
)
router.register(r"deadline", views.DeadlineViewSet, basename="deadline")
router.register(r"state", views.StateViewSet, basename="state")
router.register(r"county", views.CountyViewSet, basename="county")
router.register(r"login-credentials", LoginCredentialViewSet, basename="logins")
router.register(r"account-files", AccountFileViewSet, basename="account-file")
router.register(r"account-balance", AccountBalanceViewSet, basename="account-balance")
router.register(r"account-charge", AccountChargeViewSet, basename="account-charge")
router.register(r"payment-history", PaymentHistoryViewSet, basename="payment-history")
router.register(
    r"staff-account-balance",
    StaffAccountBalanceViewSet,
    basename="staff-account-balance",
)
router.register(r"staff-payment-history", StaffPaymentHistoryViewSet, basename="staff-payment-history")
router.register(r"payment-portal", PaymentPortalViewSet, basename="payment-portal")
router.register(r"phone-line-extension", PhoneLineExtViewSet, basename="phone-line-extension")
router.register(r"call-out", CallOutViewSet, basename="due-diligence-callout")
router.register(r"newsfeed", NewsFeedViewSet, basename="news-feed-list")


app_name = "gpg"
urlpatterns = [
    path("", include(router.urls)),
    path(
        "job-order/<int:id>/comment/",
        views.CreateJobOrderComment.as_view(),
        name="job-order-comment",
    ),
    path(
        "job-order-category/<int:id>/comment/",
        views.CreateJobOrderByApnComment.as_view(),
        name="job-order-apn-comment",
    ),
    path(
        "newsfeed/<int:id>/comment/",
        CreateNewsFeedComment.as_view(),
        name="newsfeed-comment",
    ),
]
