from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartProductForm
from .models import Cartdatabase
from django.contrib import messages
import json
from django.http import JsonResponse
# Create your views here.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    # print(cart)
    for item in cart:
        item['update_quantity_form'] = CartProductForm(
            initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_db(request, product_id):
    cart = Cartdatabase.objects.filter(product_id=product_id, user_id=1)
    # cartinsert = Cart(product_id=product_id)
    # cartinsert.save()
#    return HttpResponse("Thank")

#     # SELECT * FROM  cart WHERE (product_id = 7 AND user_id = 1)
#     # if empty
    if not cart:
        upd = Cartdatabase(product_id=product_id, user_id=1, quantity=1)
        upd.save()
        messages.success(request, 'your product has been added')
        return redirect('index')
      # return HttpResponse(" thank ")
        # return render(request, 'cart/cart.html', {'cart': cart})

    else:
        messages.error(request, 'this product is added in your cart')
        return redirect('index')

    # return render(request, 'cart/cartdetail.html', {'cart': cart})


def cartdb_details(request):
    cartdetail = Cartdatabase.objects.filter(user_id=1)
    cartamt = Cartdatabase.objects.filter(user_id=1)
    # quantity = cartdetail[0].quantity
    # print(quantity)
    cartcount = Cartdatabase.objects.filter(user_id=1).count()
    # lifeyy pahle cart count sirf cart detail ki age p aa rha tha because maine yeh
    # product = Product.objects.filter(id=product_id)
    # price = product[0].price
    # qprice = quantity*price
    # sanjhe hubyy
    amt = 0
    for cartamt in cartamt:
        q = cartamt.quantity
        amt = int(amt) + int(cartamt.product.price)*q
        # total = amt*q
        # print(amt)

    context = {
        'cartdetail': cartdetail,
        'cartcount': cartcount,
        'amt': amt,

    }

    # return JsonResponse(list(Cartdatabase.objects.filter(user_id=1).values()), safe=False)
    return render(request, 'cart/cart.html', context)


def qadd(request, cart_id):
    addq = Cartdatabase.objects.filter(id=cart_id)
    q = addq[0].quantity
    # print(q)
    add = Cartdatabase.objects.filter(id=cart_id).update(quantity=q+1)
    return redirect('cartdb_details')


def remq(request, cart_id):
    addq = Cartdatabase.objects.filter(id=cart_id)
    q = addq[0].quantity
    if q <= 1:
        remov = Cartdatabase.objects.filter(id=cart_id).delete()
    # print(q)
    add = Cartdatabase.objects.filter(id=cart_id).update(quantity=q-1)
    return redirect('cartdb_details')


# def totalcartcount(request):
#     totalcart = Cartdatabase.objects.filter(user_id=1).count()
#     #q = int(totalcart.query)
#     # return HttpResponse(q)
#     print(totalcart)
#     # lifeyy count aaa rha tha
#     context = {
#         'totalcart': totalcart,
#     }
#     return render(request, 'partials/_topbar.html', context)
