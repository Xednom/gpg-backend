from django.urls import include, path

from rest_framework import routers

from apps.forum.views import ThreadViewSet


router = routers.DefaultRouter()

router.register(r"thread", ThreadViewSet, basename="thread")

app_name = "forum"
urlpatterns = [
    path("", include(router.urls)),
]
