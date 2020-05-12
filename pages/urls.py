from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.category, name='category'),
    path('product/<int:product_id>', views.product, name='product'),
    path('search/', views.search, name='search'),


]
