from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import include, path


app_name = "auth"
urlpatterns = [
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
