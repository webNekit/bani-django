from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from .models import Gallery

# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ('image_tag', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="80" height="80" style="width:80px; height:80px; border-radius: 50%; object-fit: cover"/>'.format(obj.image.url))

    image_tag.short_description = 'Изображение'