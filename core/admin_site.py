from django.contrib.admin import AdminSite

from .models import (
    SiteSettings,
    Service,
    TeamMember,
    GalleryImage,
    QuoteRequest,
)


class BalajiMetalCoatingAdminSite(AdminSite):

    site_header = "Balaji Metal Coating LLC Admin"
    site_title = "Balaji Metal Coating LLC"
    index_title = "Website Management"

    def index(self, request, extra_context=None):

        extra_context = extra_context or {}

        settings = SiteSettings.objects.first()

        extra_context.update({

            "settings": settings,

            "service_count": Service.objects.filter(
                is_active=True
            ).count(),

            "team_count": TeamMember.objects.filter(
                is_active=True
            ).count(),

            "gallery_count": GalleryImage.objects.filter(
                is_active=True
            ).count(),

            "enquiry_count": QuoteRequest.objects.count(),

            "new_enquiry_count": QuoteRequest.objects.filter(
                status="new"
            ).count(),

            "recent_quotes": QuoteRequest.objects.order_by(
                "-created_at"
            )[:10],
        })

        return super().index(
            request,
            extra_context=extra_context
        )


uae_admin_site = BalajiMetalCoatingAdminSite(
    name="uae_admin"
)