from django.db import models

from authapp.models import User
from mainapp.models import Product

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quatity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'


    def sum(self):
        return self.quatity * self.product.price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        total = sum(basket.quatity for basket in baskets)
        return total

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        total = sum(basket.sum() for basket in baskets)
        return total