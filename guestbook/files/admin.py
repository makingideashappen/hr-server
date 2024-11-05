from django.contrib import admin
from .models import PDFFile
from .models import Photo


@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ["file", "thumbnail", "display_thumbnail"]

    def display_thumbnail(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail.url}" width="50" height="50" />'
        return "-"

    display_thumbnail.allow_tags = True
    display_thumbnail.short_description = "Thumbnail"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "uploaded_at"]
    search_fields = ["title", "description"]
