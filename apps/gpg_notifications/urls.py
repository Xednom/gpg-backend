
from django.urls import include, path
from rest_framework import routers

from apps.gpg_notifications.views import NotificationViewSet

app_name = "notifications"
urlpatterns = [
    path("alerts/", NotificationViewSet.as_view({'get': 'list'}), name="alerts")
]