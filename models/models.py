from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="имя")
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True, verbose_name="родитель"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Product(models.Model):
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='products', verbose_name="категория"
    )
    name = models.CharField(max_length=500, verbose_name="имя")
    image = models.ImageField(upload_to='product/', verbose_name="изображение")
    description = RichTextField(verbose_name="описание")
    country = models.CharField(max_length=250, verbose_name="страна")
    qty = models.IntegerField(default=0, verbose_name="количество")
    price = models.IntegerField(default=0, verbose_name="цена")
    code = models.CharField(max_length=50, verbose_name="код")
    active = models.BooleanField(default=False, verbose_name="активный")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Продукт"
