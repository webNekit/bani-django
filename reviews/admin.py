from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(ModelAdmin):
    list_display = ('pk', 'is_active')
    list_filter = ('is_active',)