from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from django.http import JsonResponse
from products.models import Product, Category


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
# print karo wifeyyyyy product ko
    # return HttpResponse(product)
    # return JsonResponse(list(Product.objects.values()), safe=False)
    return render(request, 'pages/product.html', {'product': product})
# hubby category me bhi sirf id tha na to hmne category id q liya
# samjh gyi hubyyy
# very good lifeyyyyyyy
# i love alott jaaan
# wait lifeyyy browser m print krte h
