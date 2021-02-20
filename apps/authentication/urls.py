from django.urls import include, path

from rest_framework import routers

from .views import StaffViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff-list")
router.register(r"client", ClientViewSet, basename="client-list")


app_name="auth"
urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt"))
]