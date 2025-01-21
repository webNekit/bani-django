from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Bath(models.Model):
    title = models.CharField(max_length=255, verbose_name="Введите название", help_text="Например: Баня из бруса 4х4")
    slug = models.SlugField(max_length=255, verbose_name="URL", help_text="Например: bany-4x4", unique=True)
    description_primary = RichTextField(verbose_name="Что входит в стоимость?", help_text="Введите описание", blank=False)
    description_secondary = RichTextField(verbose_name="Дополнительные работы", help_text="Введите описание", blank=False)
    width = models.IntegerField(verbose_name="Ширина", help_text="Введите ширину в метрах", blank=False)
    height = models.IntegerField(verbose_name="Высота", help_text="Введите высоту в метрах", blank=False)
    total_area = models.IntegerField(verbose_name="Общая площадь", help_text="Введите общую площадь в метрах", blank=False)
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену в рублях", blank=False)
    image = models.ImageField(upload_to='images/baths/', verbose_name="Основное изображение", blank=False, null=False)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")

    class Meta:
        verbose_name = "Баня"
        verbose_name_plural = "Бани"

    def __str__(self):
        return self.title

class BathLayout(models.Model):
    bath = models.ForeignKey(Bath, on_delete=models.CASCADE, verbose_name="Баня")
    title = models.CharField(max_length=255, verbose_name="название помещения", help_text="Например: Терраса")
    area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Площадь", help_text="Введите площадь в метрах", blank=False)

    class Meta:
        verbose_name = "Планировка"
        verbose_name_plural = "Планировки"

    def __srt__(self):
        return self.title

class BathGallery(models.Model):
    bath = models.ForeignKey(Bath, on_delete=models.CASCADE, verbose_name="Баня")
    image = models.ImageField(upload_to='images/baths/', verbose_name="Изображение", blank=False, null=False)

    class Meta:
        verbose_name = "Дополнительное изображение"
        verbose_name_plural = "Дополнительные изображения"

    def __str__(self):
        return self.bath.title