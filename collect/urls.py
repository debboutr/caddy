from django.contrib import admin
from django.urls import include, path
from junk.views import change_theme

urlpatterns = [
    path("switch-theme/", change_theme, name="change-theme"),
    path("", include("junk.urls")),
    path("admin/", admin.site.urls),
]
