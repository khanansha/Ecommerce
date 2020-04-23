from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from django.http import JsonResponse
from products.models import Product, Category, Image


def index(request):
    product = Product.objects.order_by('-pub_date')[:6]
    # SELECT * FROM `women` ORDER BY `women`.`pub_date` DESC LIMIT 3
    # return HttpResponse(women.query)
    category = Category.objects.all()
    context = {
        'product': product,
        'category': category,
    }
    return render(request, 'pages/index.html', context)


def category(request, category_id):
    product = Product.objects.filter(category_id=category_id)
    # print(product)

    return render(request, 'pages/women.html', {'product': product})


def product(request, product_id):
    product = Product.objects.filter(id=product_id)
    # select * from image WHERE product_id= product_id
    image = Image.objects.filter(product_id=product_id)
    context = {
        'product': product,
        'pro_images': image,

    }

    # return JsonResponse(list(Image.objects.values()), safe=False)
    return render(request, 'pages/product.html', context)
