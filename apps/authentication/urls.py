from django.urls import include, path

from rest_framework import routers


app_name="auth"
urlpatterns = [
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt"))
]