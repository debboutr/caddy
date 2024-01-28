from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from junk.views import change_theme

urlpatterns = [
    path("switch-theme/", change_theme, name="change-theme"),
    path("", include("junk.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
