from django.db import models
from datetime import timedelta
from django.utils.timezone import now

from authapp.models import User
from mainapp.models import Product

from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class BasketQuerySet(models.QuerySet):
    def count_gt_2(self):
        return self.filter(quatity__gt=2)

    def count_lt_2(self):
        return self.filter(quatity__lt=2)

    def delete(self):
        for object in self:
            object.refresh_quatity()
        super().delete()

    def delete_old_baskets(self):
        self.filter(created_timestamp_lt=now() - timedelta(hours=24)).delete()


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

    def delete(self, using=None, keep_parents=False):
        self.product.quatity += self.quatity
        self.product.save()
        super().delete()

    def refresh_quatity(self):
        if self.pk:
            self.quatity -= self.quatity - Basket.objects.get(pk=self.pk).quatity
        else:
            self.product.quatity -= self.quatity
        self.product.save()

    def save(self, *args):
        self.refresh_quatity()
        super().save(*args)



# @receiver(pre_save, sender=Basket)
# def product_quatity_update(sender, update_fields, instance, **kwargs):
#     if instance.pk:
#         instance.product.quatity -= instance.quatity - instance.objects.get(pk=instance.pk).quatity
#     else:
#         instance.product.quatity -= instance.quatity
#     instance.product.save()