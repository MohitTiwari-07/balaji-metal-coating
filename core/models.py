from django.db import models


class SiteSettings(models.Model):
    company_name = models.CharField(
        max_length=200,
        default="Balaji Metal Coating LLC"
    )
    tagline = models.CharField(
        max_length=255,
        blank=True
    )

    phone = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50, blank=True)
    alternate_phone = models.CharField(max_length=50, blank=True)

    email = models.EmailField()
    website = models.CharField(
        max_length=255,
        blank=True
    )

    address = models.CharField(max_length=255)

    logo = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    favicon = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    about_text = models.TextField(
        blank=True
    )

    experience_text = models.TextField(
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.company_name


class Service(models.Model):
    name = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    meta_title = models.CharField(
        max_length=200,
        blank=True
    )

    meta_description = models.CharField(
        max_length=300,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class AboutSection(models.Model):
    title = models.CharField(
        max_length=200,
        default="About Us"
    )

    content = models.TextField()

    experience_years = models.PositiveIntegerField(
        default=10
    )

    experience_title = models.CharField(
        max_length=200,
        default="Years of Experience"
    )

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    phone = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="team/", blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return f"{self.name} - {self.designation}"


class GalleryImage(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    caption = models.CharField(
        max_length=300,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["display_order", "-id"]

    def __str__(self):
        return self.title or f"Gallery Image {self.pk}"


class QuoteRequest(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        blank=True
    )

    service = models.CharField(
        max_length=200,
        blank=True
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.service or 'General Enquiry'}"