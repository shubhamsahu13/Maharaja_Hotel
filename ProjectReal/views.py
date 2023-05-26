from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from ProjectDesign.models import (
    Home,
    About,
    Chef,
    Category,
    Product,
)
from .forms import ContactForm


def home_view(request):
    home = get_object_or_404(Home, slug='maharaja-hotel')
    about = get_object_or_404(About, slug='about-us')
    chefs = get_list_or_404(Chef)
    categories = get_list_or_404(Category)
    products = get_list_or_404(Product)

    featured_products = get_list_or_404(Product, tag='featured')
    
    breakfast = get_object_or_404(Category, slug='breakfast')
    lunch = get_object_or_404(Category, slug='lunch')
    dinner = get_object_or_404(Category, slug='dinner')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ProjectReal:home-page')
    else:
        form = ContactForm()

    template_name = "ProjectReal/a-home-page.html"
    context = {
        'home': home,
        'about': about,
        'chefs': chefs,
        'categories': categories,
        'products': products,

        "featured_products": featured_products,

        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,

        'contact_form': form,
    }
    return render(request, template_name, context)

