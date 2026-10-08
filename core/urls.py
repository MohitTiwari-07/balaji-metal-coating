from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views
from .sitemaps import ServiceSitemap


sitemaps = {
    "services": ServiceSitemap,
}


urlpatterns = [
    path("", views.home, name="home"),

    path("about/", views.about, name="about"),

    path("services/", views.services, name="services"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),

    path("contact/", views.contact, name="contact"),
    path("request-quote/", views.request_quote, name="request_quote"),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django-sitemap",
    ),

    path(
        "robots.txt",
        views.robots_txt,
        name="robots_txt",
    ),

    path(
        "googleb71cd020e600215b.html",
        views.google_verification,
        name="google_verification",
    ),
]