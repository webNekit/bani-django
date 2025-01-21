from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='images/portfolio/', verbose_name="Изображение", blank=False, null=False)
    is_active = models.BooleanField(default=True, verbose_name='Отображать на сайте')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение #{self.pk}"