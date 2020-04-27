from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.category

    @property
    def get_products(self):
        return Product.objects.filter(category_id=self.id).order_by('-pub_date')[:3]

        # return str(self.id)


Select_size = (
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('SM', 'SMALL'),
    ('LG', 'LARGE'),
    ('MD', 'MEDIUM'),
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    sizes = MultiSelectField(choices=Select_size, default='')
    image = models.ImageField(upload_to='products/images', default="")

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='Product')
    images = models.ImageField(upload_to='product/images', default="")
