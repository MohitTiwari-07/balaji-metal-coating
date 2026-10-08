from django.contrib import admin

from .admin_site import uae_admin_site

from .models import (
    SiteSettings,
    Service,
    AboutSection,
    TeamMember,
    GalleryImage,
    QuoteRequest,
)


class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "phone",
        "email",
        "address",
        "updated_at",
    )

    search_fields = (
        "company_name",
        "phone",
        "email",
        "address",
    )

    readonly_fields = (
        "updated_at",
    )

    fieldsets = (
        (
            "Company Information",
            {
                "fields": (
                    "company_name",
                    "tagline",
                    "website",
                )
            }
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "phone",
                    "whatsapp",
                    "alternate_phone",
                    "email",
                    "address",
                )
            }
        ),
        (
            "Branding",
            {
                "fields": (
                    "logo",
                    "favicon",
                )
            }
        ),
        (
            "Website Content",
            {
                "fields": (
                    "about_text",
                    "experience_text",
                )
            }
        ),
        (
            "System Information",
            {
                "fields": (
                    "updated_at",
                )
            }
        ),
    )


class ServiceAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_display = (
        "name",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "short_description",
        "description",
        "meta_title",
        "meta_description",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "name",
    )

    fieldsets = (
        (
            "Service Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "short_description",
                    "description",
                    "image",
                    "display_order",
                    "is_active",
                )
            }
        ),
        (
            "SEO Settings",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                ),
                "classes": ("collapse",),
            }
        ),
    )


class AboutSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "experience_years",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "content",
        "experience_title",
    )

    list_editable = (
        "experience_years",
        "is_active",
    )


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "phone", "display_order", "is_active")
    list_filter = ("designation", "is_active")
    search_fields = ("name", "designation", "phone", "description")
    list_editable = ("display_order", "is_active")
    ordering = ("display_order", "name")

    fieldsets = (
        (
            "Team Member Information",
            {
                "fields": (
                    "name",
                    "designation",
                    "phone",
                    "description",
                    "image",
                    "display_order",
                    "is_active",
                )
            },
        ),
    )


class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "caption",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "-id",
    )


class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "service",
        "phone",
        "email",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "service",
        "message",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )


# Register models with Balaji Metal Coating custom admin site

uae_admin_site.register(
    SiteSettings,
    SiteSettingsAdmin
)

uae_admin_site.register(
    Service,
    ServiceAdmin
)

uae_admin_site.register(
    AboutSection,
    AboutSectionAdmin
)

uae_admin_site.register(
    TeamMember,
    TeamMemberAdmin
)

uae_admin_site.register(
    GalleryImage,
    GalleryImageAdmin
)

uae_admin_site.register(
    QuoteRequest,
    QuoteRequestAdmin
)