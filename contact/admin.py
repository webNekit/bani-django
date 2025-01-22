from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(ModelAdmin):
    list_display = ('phone_number', 'email', 'working_hours', 'updated_at')

    def has_add_permission(self, request):
        # Запрещаем добавление новой записи, если уже существует хотя бы одна
        return not ContactInfo.objects.exists()