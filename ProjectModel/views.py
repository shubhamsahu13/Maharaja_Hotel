from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from ProjectDesign.models import (
    Home,
    Category,
    Product,
)


def home_view(request):
    home = get_object_or_404(Home, title='The Young Baker')
    categories = get_list_or_404(Category)
    featured_products = get_list_or_404(Product, tag='featured')

    template_name = 'ProjectModel/a-home-page.html'
    context = {
        'title': 'Home',
        'home': home,
        'categories': categories,
        'featured_products':featured_products,
    }
    return render(request, template_name, context)


def product_retrieve_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectModel/b-product-retrieve-page.html'
    context = {
        'title': f'Product - {product.title}',
        'product': product,
    }
    return render(request, template_name, context)