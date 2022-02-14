from django.urls import include, path
from rest_framework import routers

from apps.gpg_notifications.views import NotificationViewSet

router = routers.DefaultRouter()

router.register(r"alerts", NotificationViewSet, basename="alert")

app_name = "notifications"
urlpatterns = [path("", include(router.urls))]
