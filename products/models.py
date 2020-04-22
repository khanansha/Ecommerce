from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/images', default="")

    def __str__(self):
        return self.name
