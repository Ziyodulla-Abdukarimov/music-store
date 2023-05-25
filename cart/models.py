from django.db import models
from common.models import BaseModel
from config import settings
from models.models import Product
from django.db.models import F, Sum


# Create your models here.
class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', blank=True,
                                null=True, verbose_name="пользователь")
    cart_id_pk = models.CharField(max_length=300, blank=True, null=True, verbose_name="Идентификатор корзины")

    class Meta:
        verbose_name_plural = "Корзина"

    def __str__(self):
        return str(self.user)


class StatusChoice(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = 'inactive'


class CartItem(BaseModel):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE, related_name='items', verbose_name="Корзина")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items', verbose_name="продукт")
    quantity = models.PositiveIntegerField(default=1, verbose_name="количество")
    status = models.CharField(max_length=8, choices=StatusChoice.choices, default=StatusChoice.ACTIVE,
                              verbose_name="положение дел")

    @staticmethod
    def get_total_price():
        return CartItem.objects.annotate(item_price=F('product__price') * F('quantity')).aggregate(
            total_price=Sum('item_price'))['total_price'] or 0

    @staticmethod
    def get_total_qty():
        return CartItem.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']

    class Meta:
        verbose_name_plural = "Корзина товаров"
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.product)
