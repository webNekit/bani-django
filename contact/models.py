from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=22, verbose_name="Номер телефона", help_text="Например: +78007776655", blank=False)
    phone_format = models.CharField(max_length=255, verbose_name="Формат номера телефона", help_text="Например: +7(800)777-66-55", blank=False)
    email = models.EmailField(verbose_name="Адрес эл.почты", help_text="Например: info@company.ru", blank=False)
    social_vk = models.URLField(verbose_name="Вконтакте", help_text="Вставьте url-ссылку сообщества вконтакте", blank=True, null=True)
    social_tg = models.URLField(verbose_name="Телеграм", help_text="Вставьте url-ссылку сообщества телеграм", blank=True, null=True)
    social_youtube = models.URLField(verbose_name="YouTube", help_text="Вставьте url-ссылку сообщества Youtube", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес", help_text="Например: г. Москва, ул. Пушкина, д. 1", blank=False)
    working_hours = models.CharField(max_length=255,  verbose_name="График работы", help_text="Например: Ежедневно с 9.00 до 21.00")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"Контактная информация (обновлено {self.updated_at})"
