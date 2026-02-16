from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, Audio, Gallery, Sandhya, Aromal


# reusable preview function
class ImagePreviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'preview')
    readonly_fields = ('preview',)
    ordering = ('-id',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" style="border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    preview.short_description = "Preview"


@admin.register(Banner)
class BannerAdmin(ImagePreviewAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(ImagePreviewAdmin):
    pass


@admin.register(Sandhya)
class SandhyaAdmin(ImagePreviewAdmin):
    pass


@admin.register(Aromal)
class AromalAdmin(ImagePreviewAdmin):
    pass


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')
    ordering = ('-id',)
