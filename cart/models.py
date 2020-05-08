from django.db import models
from products.models import Product
# Create your models here.


class Cartdatabase(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='Productcart')
    created_at = models.DateField(auto_now=True)
    quantity = models.IntegerField(default=1)
    #price = models.CharField(max_length=100, default='')
    user_id = models.IntegerField(default=1)

    # @property
    # def get_cartproduct(self):
    #     return Product.objects.filter(id=self.id)
