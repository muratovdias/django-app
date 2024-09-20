from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import *


def index(request):

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'base.html', context=context)


def category_detail(request, cat_slug):

    cat = get_object_or_404(Category, slug=cat_slug)
    products = Product.objects.filter(category=cat, is_published=True)
    categories = Category.objects.all()
    cat_selected = cat.pk
    context = {
        'products': products,
        'categoriya': cat,
        'categories': categories,
        'cat_selected': cat_selected
    }
    return render(request, 'category_detail.html', context=context)


def product_detail(request, prod_slug):

    product = Product.objects.filter(slug=prod_slug)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'product': product[0]
    }
    return render(request, 'product_detail.html', context=context)


def delivery(request):

    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'delivery.html', context=context)


def services(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'services.html', context=context)


def about(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'about.html', context=context)


def contacts(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'contacts.html', context=context)
