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
    # select * from category
    # select *  from category LIMIT 3
    category = Category.objects.all()
    cat_slider = Category.objects.all()[:3]
    context = {
        'product': product,
        'category': category,
        'cat_slider': cat_slider,
    }
    #Department.objects.filter(departmentvolunteer__isnull=True).values_list('name', flat=True)
    # return JsonResponse(list(Product.objects.select_related('product_id').values()), safe=False)
    # p = Product.objects.filter(
    # category_id=2).values_list('category', flat=True)
    # return HttpResponse(p.query)
    # print(p.query)
    # return JsonResponse(list(Product.objects.filter(category_id=2).values_list('category', flat=True)).values(), safe=False)
    # return JsonResponse(list(Product.objects.values()), safe=False)
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
    # return JsonResponse(list(Product.objects.filter(id=product_id).values()), safe=False)
    # return JsonResponse(list(Image.objects.values()), safe=False)
    return render(request, 'pages/product.html', context)


def cart(request):
    return render(request, 'pages/cart.html')
