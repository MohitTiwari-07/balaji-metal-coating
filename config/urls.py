from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from core.admin_site import uae_admin_site


urlpatterns = [
    path("admin/", uae_admin_site.urls),
    path("", include("core.urls")),
]

handler404 = "core.views.custom_404"

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )