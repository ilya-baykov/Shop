from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'products': products, 'categories': categories, 'category': category})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
