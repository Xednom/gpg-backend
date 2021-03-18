from django.urls import include, path
from rest_framework import routers

from apps.authentication.views import (
    StaffViewSet,
    ClientViewSet,
    ClientFilesViewSet,
    StaffFilesViewSet,
)
from . import views

router = routers.DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff-list")
router.register(r"client", ClientViewSet, basename="client-list")
router.register(r"client-files", ClientFilesViewSet, basename="client-files-list")
router.register(r"staff-files", StaffFilesViewSet, basename="staff-files-list")
router.register(
    r"job-order", views.JobOrderGeneralViewSet, basename="job-order-general"
)
router.register(
    r"job-order-by-category", views.JobOrderByCategoryViewSet, basename="job-order-category"
)
router.register(
    r"property-detail", views.PropertyDetailsViewSet, basename="property-details"
)
router.register(r"apn-category-type", views.ApnCategoryViewSet, basename="apn-category-types")


app_name = "gpg"
urlpatterns = [
    path("", include(router.urls)),
    path("job-order/<int:id>/comment/", views.CreateJobOrderComment.as_view(), name="job-order-comment"),
    path("job-order-category/<int:id>/comment/", views.CreateJobOrderByApnComment.as_view(), name="job-order-apn-comment")
]
