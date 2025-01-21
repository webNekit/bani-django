from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from .models import Bath, BathLayout, BathGallery

class BathLayoutInline(TabularInline):
    model = BathLayout
    extra = 1

class BathGalleryInline(TabularInline):
    model = BathGallery
    extra = 1

@admin.register(Bath)
class BathAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'slug']
    list_filter = ['is_active']
    inlines = [BathLayoutInline, BathGalleryInline]
