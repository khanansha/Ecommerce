from django.contrib import admin
# password admin12345
# usename admin

from .models import Product, Category, Image


class imagesInline(admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True
    #classes = ['collapse']


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    inlines = [imagesInline]


admin.site.register(Product, ProductAdmin)

admin.site.register(Category)
