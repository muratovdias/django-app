from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('delivery', delivery, name='delivery'),
    path('services', services, name='services'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('category/<slug:cat_slug>/', category_detail, name='categoris'),
    path('product/<slug:prod_slug>/', product_detail, name='product')
]
