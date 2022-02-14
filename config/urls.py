"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
import notifications.urls

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

MEDIA_URL = settings.MEDIA_URL.replace("http://127.0.0.1:8000", "")

urlpatterns = [
    path("grappelli", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("apps.authentication.urls")),
    path("api/v1/", include("apps.gpg.urls")),
    path("api/v1/", include("apps.gpg_notifications.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path(
        "inbox/notifications/",
        include(notifications.urls, namespace="hq-notifications"),
    ),
] + static(MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "G.P.G Corp Management System Admin site"
admin.site.site_header = "G.P.G Corp. Management System"
