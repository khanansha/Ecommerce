from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from django.http import JsonResponse
from products.models import Product, Category, Image
from cart.forms import CartAddProductForm


def index(request):
    product = Product.objects.order_by('-pub_date')[:6]

    # SELECT * FROM `women` ORDER BY `women`.`pub_date` DESC LIMIT 3
    # return HttpResponse(women.query)
    # select * from category
    # select *  from category LIMIT 3
    category = Category.objects.all()
    cat_slider = Category.objects.all()[:3]
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'category': category,
        'cat_slider': cat_slider,
        'cart_product_form': cart_product_form,
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
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,

    }

    return render(request, 'pages/women.html', context)


def product(request, product_id):
    product = Product.objects.filter(id=product_id)
    # select * from image WHERE product_id= product_id
    image = Image.objects.filter(product_id=product_id)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'pro_images': image,
        'cart_product_form': cart_product_form,

    }
    # return JsonResponse(list(Product.objects.filter(id=product_id).values()), safe=False)
    # return JsonResponse(list(Image.objects.values()), safe=False)
    return render(request, 'pages/product.html', context)


# def cart(request):
#     return render(request, 'pages/cart.html')

def search(request):
    # select * from Product ODER BY 'list_date' DESC
    queryset_list = Product.objects.order_by('-pub_date')
   # return HttpResponse(queryset_list.query)
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
           # SELECT name FROM product WHERE name CONTAINS 'word1 word2 word3...'
            queryset_list = queryset_list.filter(
                name__icontains=keywords)
            # return HttpResponse(queryset_list.query)
    context = {
        'product': queryset_list,
        'values': request.GET,
    }
    return render(request, 'pages/search.html', context)
