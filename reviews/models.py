from django.db import models

# Create your models here.
class Reviews(models.Model):
    video = models.FileField(upload_to='videos/', verbose_name='Видеоотзыв')
    is_active = models.BooleanField(default=True, verbose_name='Отображать на сайте')

    class Meta:
        verbose_name = "Видеоотзыв"
        verbose_name_plural = "Видеоотзывы"

    def __str__(self):
        return f"Видеоотзыв #{self.pk}"