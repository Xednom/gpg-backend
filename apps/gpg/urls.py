from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"job-order", views.JobOrderGeneralViewSet, basename="job-order-general")


app_name="gpg"
urlpatterns = [
    path("", include(router.urls))
]