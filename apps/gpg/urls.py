from django.urls import include, path
from rest_framework import routers

from apps.authentication.views import StaffViewSet, ClientViewSet, ClientFilesViewSet, StaffFilesViewSet
from . import views

router = routers.DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff-list")
router.register(r"client", ClientViewSet, basename="client-list")
router.register(r"client-files", ClientFilesViewSet, basename="client-files-list")
router.register(r"staff-files", StaffFilesViewSet, basename="staff-files-list")
router.register(r"job-order", views.JobOrderGeneralViewSet, basename="job-order-general")


app_name="gpg"
urlpatterns = [
    path("", include(router.urls))
]