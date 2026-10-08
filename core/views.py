from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

import json
import urllib.request

from .models import (
    Service,
    QuoteRequest,
    SiteSettings,
    AboutSection,
    TeamMember,
    GalleryImage,
)


# =========================================================
# HOME
# =========================================================

def home(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        service = request.POST.get("service", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not phone:
            messages.error(
                request,
                "Please enter your name and phone number."
            )
            return redirect("home")

        quote = QuoteRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            service=service,
            message=message,
        )

        send_quote_email(quote)

        messages.success(
            request,
            "Thank you! Your enquiry has been submitted successfully."
        )

        return redirect("home")

    site_settings = SiteSettings.objects.first()

    services = Service.objects.filter(
        is_active=True
    )

    about_section = AboutSection.objects.filter(
        is_active=True
    ).first()

    team_members = TeamMember.objects.filter(
        is_active=True
    )

    gallery_images = GalleryImage.objects.filter(
        is_active=True
    )

    return render(
        request,
        "home.html",
        {
            "settings": site_settings,
            "services": services,
            "about_section": about_section,
            "team_members": team_members,
            "gallery_images": gallery_images,
        }
    )


# =========================================================
# SERVICES
# =========================================================

def services(request):

    site_settings = SiteSettings.objects.first()

    service_list = Service.objects.filter(
        is_active=True
    )

    return render(
        request,
        "services.html",
        {
            "settings": site_settings,
            "services": service_list,
        }
    )


# =========================================================
# SERVICE DETAIL
# =========================================================

def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True
    )

    site_settings = SiteSettings.objects.first()

    services_list = Service.objects.filter(
        is_active=True
    )

    return render(
        request,
        "service_detail.html",
        {
            "settings": site_settings,
            "service": service,
            "services": services_list,
        }
    )


# =========================================================
# ABOUT
# =========================================================

def about(request):

    site_settings = SiteSettings.objects.first()

    about_section = AboutSection.objects.filter(
        is_active=True
    ).first()

    team_members = TeamMember.objects.filter(
        is_active=True
    )

    return render(
        request,
        "about.html",
        {
            "settings": site_settings,
            "about_section": about_section,
            "team_members": team_members,
        }
    )


# =========================================================
# CONTACT
# =========================================================

# =========================================================
# CONTACT
# =========================================================

def contact(request):

    site_settings = SiteSettings.objects.first()

    service_list = Service.objects.filter(
        is_active=True
    )

    team_members = TeamMember.objects.filter(
        is_active=True
    )

    return render(
        request,
        "contact.html",
        {
            "settings": site_settings,
            "services": service_list,
            "team_members": team_members,
        }
    )


# =========================================================
# REQUEST QUOTE
# =========================================================

def request_quote(request):

    site_settings = SiteSettings.objects.first()

    service_list = Service.objects.filter(
        is_active=True
    )

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        service = request.POST.get("service", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not phone:

            messages.error(
                request,
                "Please enter your name and phone number."
            )

            return render(
                request,
                "request_quote.html",
                {
                    "settings": site_settings,
                    "services": service_list,
                }
            )

        quote = QuoteRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            service=service,
            message=message,
        )

        send_quote_email(quote)

        messages.success(
            request,
            "Thank you! Your enquiry has been submitted successfully."
        )

        return redirect("request_quote")

    return render(
        request,
        "request_quote.html",
        {
            "settings": site_settings,
            "services": service_list,
        }
    )


# =========================================================
# ROBOTS.TXT
# =========================================================

def robots_txt(request):

    site_settings = SiteSettings.objects.first()

    website = "https://balajimetalcoating.com"

    if site_settings and site_settings.website:

        website = site_settings.website.strip()

        if not website.startswith("http"):
            website = f"https://{website}"

        website = website.rstrip("/")

    content = f"""User-agent: *
Allow: /

Sitemap: {website}/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )


# =========================================================
# GOOGLE VERIFICATION
# =========================================================

def google_verification(request):

    file_path = settings.BASE_DIR / "googleb71cd020e600215b.html"

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        return HttpResponse(
            content,
            content_type="text/html"
        )

    except FileNotFoundError:

        return HttpResponse(
            "Verification file not found.",
            status=404
        )


# =========================================================
# CUSTOM 404
# =========================================================

def custom_404(request, exception):

    site_settings = SiteSettings.objects.first()

    return render(
        request,
        "404.html",
        {
            "settings": site_settings,
        },
        status=404
    )


# =========================================================
# SEND ENQUIRY EMAIL
# =========================================================

def send_quote_email(quote):

    try:

        api_key = getattr(
            settings,
            "RESEND_API_KEY",
            None
        )

        if not api_key:

            print(
                "RESEND ERROR: RESEND_API_KEY is missing"
            )

            return

        site_settings = SiteSettings.objects.first()

        if not site_settings:

            print(
                "RESEND ERROR: SiteSettings not found"
            )

            return

        recipient = site_settings.email

        if not recipient:

            print(
                "RESEND ERROR: SiteSettings email is empty"
            )

            return

        company_name = (
            site_settings.company_name
            or "Balaji Metal Coating LLC"
        )

        data = {

            "from": (
                f"{company_name} "
                "<onboarding@resend.dev>"
            ),

            "to": [
                recipient
            ],

            "subject": (
                f"New Enquiry - "
                f"{quote.service or 'General Enquiry'}"
            ),

            "html": f"""
                <div style="
                    font-family:Arial,sans-serif;
                    max-width:650px;
                    margin:auto;
                    padding:25px;
                    border:1px solid #ddd;
                    border-radius:10px;
                ">

                    <h2>New Website Enquiry</h2>

                    <hr>

                    <p>
                        <strong>Name:</strong>
                        {quote.name}
                    </p>

                    <p>
                        <strong>Phone:</strong>
                        {quote.phone}
                    </p>

                    <p>
                        <strong>Email:</strong>
                        {quote.email or "Not provided"}
                    </p>

                    <p>
                        <strong>Service:</strong>
                        {quote.service or "General Enquiry"}
                    </p>

                    <p>
                        <strong>Message:</strong>
                    </p>

                    <p>
                        {quote.message or "No message provided"}
                    </p>

                    <hr>

                    <p>
                        {company_name} Website
                    </p>

                </div>
            """
        }

        api_request = urllib.request.Request(

            "https://api.resend.com/emails",

            data=json.dumps(data).encode("utf-8"),

            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },

            method="POST"
        )

        with urllib.request.urlopen(
            api_request,
            timeout=8
        ) as response:

            result = response.read().decode("utf-8")

            print(
                "RESEND SUCCESS:",
                result
            )

    except Exception as e:

        print(
            "RESEND EMAIL ERROR:",
            repr(e)
        )