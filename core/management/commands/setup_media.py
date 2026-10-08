import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import AboutSection, Service, GalleryImage


class Command(BaseCommand):
    help = "Copy optimized media files and assign them to About, Services and Gallery"

    def handle(self, *args, **options):

        base_dir = Path(settings.BASE_DIR)
        seed_media = base_dir / "seed_media"
        media_root = Path(settings.MEDIA_ROOT)

        if not seed_media.exists():
            self.stdout.write(
                self.style.ERROR(
                    f"seed_media folder not found: {seed_media}"
                )
            )
            return

        media_root.mkdir(parents=True, exist_ok=True)

        # COPY ALL MEDIA FILES
        for source_file in seed_media.rglob("*"):
            if not source_file.is_file():
                continue

            relative_path = source_file.relative_to(seed_media)
            destination = media_root / relative_path

            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, destination)

        # ABOUT IMAGE
        about_folder = media_root / "about"

        about_images = (
            sorted(
                [p for p in about_folder.glob("*") if p.is_file()]
            )
            if about_folder.exists()
            else []
        )

        about = AboutSection.objects.filter(is_active=True).first()

        if about and about_images:
            about.image.name = str(
                about_images[0].relative_to(media_root)
            )
            about.save(update_fields=["image"])

            self.stdout.write(
                self.style.SUCCESS(
                    "About image assigned successfully."
                )
            )

        # SERVICE IMAGES
        service_folder = media_root / "services"

        service_images = (
            sorted(
                [p for p in service_folder.glob("*") if p.is_file()]
            )
            if service_folder.exists()
            else []
        )

        services = list(
            Service.objects.order_by("display_order", "name")
        )

        for service, image_path in zip(services, service_images):

            service.image.name = str(
                image_path.relative_to(media_root)
            )

            service.save(update_fields=["image"])

            self.stdout.write(
                self.style.SUCCESS(
                    f"Service image assigned: {service.name}"
                )
            )

        # GALLERY IMAGES
        gallery_folder = media_root / "gallery"

        gallery_images = (
            sorted(
                [p for p in gallery_folder.glob("*") if p.is_file()]
            )
            if gallery_folder.exists()
            else []
        )

        if gallery_images:

            GalleryImage.objects.all().delete()

            for index, image_path in enumerate(
                gallery_images,
                start=1
            ):

                GalleryImage.objects.create(
                    title=f"Balaji Metal Coating Work {index}",
                    image=str(
                        image_path.relative_to(media_root)
                    ),
                    display_order=index,
                    is_active=True,
                )

            self.stdout.write(
                self.style.SUCCESS(
                    f"{len(gallery_images)} gallery images added successfully."
                )
            )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "Media setup completed successfully."
            )
        )