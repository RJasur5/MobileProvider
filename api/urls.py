from django.urls import path
from .views import *

urlpatterns = [
    path('products', allproducts, name='products'),
    path('product/detail/<int:pk>', product_detail),
]