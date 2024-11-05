from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File as DjangoFile


class PDFFile(models.Model):
    file = models.FileField(upload_to="pdfs/")
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.file:
            self.generate_thumbnail()
        super().save(*args, **kwargs)

    def generate_thumbnail(self):
        try:
            image = Image.open(self.file)
            image.thumbnail((128, 128))  # Resize to a thumbnail
            thumb_io = BytesIO()
            image.save(thumb_io, format="PNG")
            thumbnail_name = self.file.name.replace("pdfs/", "thumbnails/").replace(
                ".pdf", ".png"
            )
            self.thumbnail.save(thumbnail_name, DjangoFile(thumb_io), save=False)
        except Exception as e:
            print(f"Error generating thumbnail: {e}")

    def __str__(self):
        return self.file.name.split("/")[-1]


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="photos/")
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Photo {self.id}"
