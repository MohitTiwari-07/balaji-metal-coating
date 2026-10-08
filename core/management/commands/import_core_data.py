from django.core.management.base import BaseCommand
from core.models import (
    SiteSettings,
    Service,
    AboutSection,
    TeamMember,
    QuoteRequest,
)


class Command(BaseCommand):
    help = "Reset and seed Balaji Metal Coating website content"

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.WARNING(
                "Starting Balaji Metal Coating content setup..."
            )
        )

        # ---------------------------------------------------------
        # OLD ENQUIRIES
        # ---------------------------------------------------------
        enquiry_count = QuoteRequest.objects.count()

        if enquiry_count:
            QuoteRequest.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Deleted {enquiry_count} old enquiries."
                )
            )

        # ---------------------------------------------------------
        # SERVICES
        # ---------------------------------------------------------
        Service.objects.all().delete()

        services = [
    {
        "name": "Gold Plating",
        "slug": "gold-plating",
        "short_description": "Professional gold plating solutions.",
        "description": "Professional gold plating services for different metal surfaces and coating requirements.",
        "display_order": 1,
    },
    {
        "name": "Nickel Plating",
        "slug": "nickel-plating",
        "short_description": "Professional nickel plating solutions.",
        "description": "Nickel plating services for different metal surfaces and finishing requirements.",
        "display_order": 2,
    },
    {
        "name": "Brass Plating",
        "slug": "brass-plating",
        "short_description": "Professional brass plating solutions.",
        "description": "Brass plating services for different metal coating and finishing requirements.",
        "display_order": 3,
    },
    {
        "name": "Rusted Plating",
        "slug": "rusted-plating",
        "short_description": "Rusted finish and coating solutions.",
        "description": "Rusted finish and coating work according to project requirements.",
        "display_order": 4,
    },
    {
        "name": "Bronze Plating",
        "slug": "bronze-plating",
        "short_description": "Professional bronze plating solutions.",
        "description": "Bronze plating services for different metal surfaces and finishing requirements.",
        "display_order": 5,
    },
    {
        "name": "Silver Plating",
        "slug": "silver-plating",
        "short_description": "Professional silver plating solutions.",
        "description": "Silver plating services for different metal coating and finishing requirements.",
        "display_order": 6,
    },
    {
        "name": "Copper Plating",
        "slug": "copper-plating",
        "short_description": "Professional copper plating solutions.",
        "description": "Copper plating services for different metal surfaces and coating requirements.",
        "display_order": 7,
    },
    {
        "name": "Black Nickel Plating",
        "slug": "black-nickel-plating",
        "short_description": "Professional black nickel plating solutions.",
        "description": "Black nickel plating services for decorative and metal finishing requirements.",
        "display_order": 8,
    },
    {
        "name": "Powder Coating",
        "slug": "powder-coating",
        "short_description": "Professional powder coating solutions.",
        "description": "Powder coating work for different metal surfaces and finishing requirements.",
        "display_order": 9,
    },
    {
        "name": "Antique Brass",
        "slug": "antique-brass",
        "short_description": "Antique brass finishing solutions.",
        "description": "Antique brass finishing work for different metal surfaces and decorative requirements.",
        "display_order": 10,
    },
]

        for service_data in services:
         Service.objects.create(
            is_active=True,
           **service_data,
    )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(services)} metal coating services."
            )
        )

        # ---------------------------------------------------------
        # SITE SETTINGS
        # ---------------------------------------------------------
        settings = SiteSettings.objects.first()

        if settings is None:
            settings = SiteSettings()

        settings.company_name = "Balaji Metal Coating LLC"
        settings.tagline = "Metal Coating & Plating Solutions"
        settings.phone = "+971 52 209 5781"
        settings.whatsapp = "+971 52 209 5781"
        settings.alternate_phone = "+971 55 689 3788 / +971 56 360 4345"
        settings.email = "info@balajimetalcoating.com"
        settings.website = "www.balajimetalcoating.com"
        settings.address = "Jabal Ali Industrial Area-1, Dubai, UAE"

        settings.about_text = (
            "Balaji Metal Coating LLC is a Dubai-based metal coating company "
            "with experience in metal coating and plating work. The company "
            "provides different types of metal coating services for customers "
            "in Dubai."
        )

        settings.experience_text = (
            "With more than 10 years of experience in interior designing "
            "and metal coating, the team has developed experience across "
            "different fields in Dubai."
        )

        settings.save()

        self.stdout.write(
            self.style.SUCCESS("Company settings updated.")
        )

        # ---------------------------------------------------------
        # ABOUT SECTION
        # ---------------------------------------------------------
        AboutSection.objects.all().delete()

        AboutSection.objects.create(
            title="About Balaji Metal Coating LLC",
            content=(
                "Balaji Metal Coating LLC is a well-experienced metal coating "
                "company based in Dubai, UAE. The company provides different "
                "types of metal coating and plating services."
            ),
            experience_years=10,
            experience_title="Years of Experience",
            is_active=True,
        )

        self.stdout.write(
            self.style.SUCCESS("About section created.")
        )

        # ---------------------------------------------------------
        # TEAM
        # ---------------------------------------------------------
        TeamMember.objects.all().delete()

        team_members = [
    {
        "name": "Kushal Ram",
        "designation": "Sales Officer",
        "phone": "+971 54 593 9612",
        "description": "",
        "display_order": 1,
    },
    {
        "name": "Santosh Nishad",
        "designation": "Business Partner",
        "phone": "+971 50 109 7411",
        "description": "",
        "display_order": 2,
    },
    {
        "name": "Aaidman Ram Jhakar",
        "designation": "Business Partner",
        "phone": "+971 52 527 2955",
        "description": "",
        "display_order": 3,
    },
]

        for member in team_members:
         TeamMember.objects.create(
          is_active=True,
          **member,
    )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(team_members)} team members."
            )
        )

        # ---------------------------------------------------------
        # FINAL SUMMARY
        # ---------------------------------------------------------
        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "=============================================="
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "Balaji Metal Coating content setup completed."
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "Services: 10"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "Team members: 3"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "About section: 1"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "Old enquiries: removed"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "=============================================="
            )
        )