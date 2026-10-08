from django.contrib.sitemaps import Sitemap

from .models import Service


class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Service.objects.filter(is_active=True)

    def location(self, obj):
        return f"/services/{obj.slug}/"