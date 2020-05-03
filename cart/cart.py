from decimal import Decimal
from django.conf import settings
from products.models import Product
import json
from django.http import JsonResponse
from django.http import HttpResponse


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
#       print(product_id)
        # output: 7
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
           # print(self.cart[product_id])
            # output :{'quantity': 0, 'price': '1500'}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        # select * from Product where id = 1,2,3, ..
        # print(products.query)
        # return JsonResponse(list(Product.objects.filter(id__in=product_ids).values()), safe=False)
        for product in products:
            self.cart[str(product.id)]['product'] = product
            # print(self.cart[str(product.id)]['product'])
            # output :Browen TShirts ,Cool Clothing with Brown Stripes,men,men,mens
            # return JsonResponse(list(self.cart[str(product.id)]['product'].values()), safe=False)

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        # return JsonResponse(list(sum(item['quantity'] for item in self.cart.values())), safe=False)
        return sum(item['quantity'] for item in self.cart.values())
        # return HttpResponse(list(sum(item['quantity'] for item in self.cart.values())))
        #print(sum(item['quantity'] for item in self.cart.values()))

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
