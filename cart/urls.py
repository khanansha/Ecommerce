from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart_db/<int:product_id>', views.cart_db, name='cart_db'),
    path('cartdb_details/', views.cartdb_details, name='cartdb_details'),
    path('qadd/<int:cart_id>', views.qadd, name='qadd'),
    path('remq/<int:cart_id>', views.remq, name='remq'),
    # path('totalcartcount/', views.totalcartcount, name='totalcartcount'),


]
