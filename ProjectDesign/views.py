from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import (
    Home,
    Category,
    Product,
    About,
)
from .forms import (
    HomeForm,
    CategoryForm,
    ProductForm,
    AboutForm,
)


# Entry
def entry_view(request):
    template_name = 'ProjectDesign/entry-page.html'
    context = {
        'title': 'Entry Page'
    }
    return render(request, template_name, context)


# Home Model (LCRUD)
# Home List
@staff_member_required()
def home_list_view(request):
    objects_list = Home.objects.all()

    template_name = 'ProjectDesign/Home/a-home-list-page.html'
    context = {
        'title': 'Home List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Home Create
@staff_member_required()
def home_create_view(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:home-list-page')
    else:
        form = HomeForm()

    template_name = 'ProjectDesign/Home/b-home-create-page.html'
    context = {
        'title': 'Home Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Home Retrieve
@staff_member_required()
def home_retrieve_view(request, slug):
    object = get_object_or_404(Home, slug=slug)

    template_name = 'ProjectDesign/Home/c-home-retrieve-page.html'
    context = {
        'title': 'Home Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Home Update
@staff_member_required()
def home_update_view(request, slug):
    object = get_object_or_404(Home, slug=slug)

    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:home-list-page')
    else:
        form = HomeForm(instance=object)

    template_name = 'ProjectDesign/Home/d-home-update-page.html'
    context = {
        'title': 'Home Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Home Delete
@staff_member_required()
def home_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Home, slug=slug)
        object.delete()
        return redirect('ProjectDesign:home-list-page')
    else:
        object = get_object_or_404(Home, slug=slug)

    template_name = 'ProjectDesign/Home/e-home-delete-page.html'
    context = {
        'title': 'Home Delete',
        'object': object,
    }
    return render(request, template_name, context)


# Category Model (LCRUD)
# Category List
@staff_member_required()
def category_list_view(request):
    objects_list = Category.objects.all()

    template_name = 'ProjectDesign/Category/a-category-list-page.html'
    context = {
        'title': 'Category List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Category Create
@staff_member_required()
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:category-list-page')
    else:
        form = CategoryForm()

    template_name = 'ProjectDesign/Category/b-category-create-page.html'
    context = {
        'title': 'Category Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Category Retrieve
@staff_member_required()
def category_retrieve_view(request, slug):
    object = get_object_or_404(Category, slug=slug)

    template_name = 'ProjectDesign/Category/c-category-retrieve-page.html'
    context = {
        'title': 'Category Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Category Update
@staff_member_required()
def category_update_view(request, slug):
    object = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:category-list-page')
    else:
        form = CategoryForm(instance=object)

    template_name = 'ProjectDesign/Category/d-category-update-page.html'
    context = {
        'title': 'Category Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Category Delete
@staff_member_required()
def category_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Category, slug=slug)
        object.delete()
        return redirect('ProjectDesign:category-list-page')
    else:
        object = get_object_or_404(Category, slug=slug)

    template_name = 'ProjectDesign/Category/e-category-delete-page.html'
    context = {
        'title': 'Category Delete',
        'object': object,
    }
    return render(request, template_name, context)


# Product Model (LCRUD)
# Product List
@staff_member_required()
def product_list_view(request):
    objects_list = Product.objects.all()

    template_name = 'ProjectDesign/Product/a-product-list-page.html'
    context = {
        'title': 'Product List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Product Create
@staff_member_required()
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:product-list-page')
    else:
        form = ProductForm()

    template_name = 'ProjectDesign/Product/b-product-create-page.html'
    context = {
        'title': 'Product Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Product Retrieve
@staff_member_required()
def product_retrieve_view(request, slug):
    object = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectDesign/Product/c-product-retrieve-page.html'
    context = {
        'title': 'Product Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Product Update
@staff_member_required()
def product_update_view(request, slug):
    object = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:product-list-page')
    else:
        form = ProductForm(instance=object)

    template_name = 'ProjectDesign/Product/d-product-update-page.html'
    context = {
        'title': 'Product Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Product Delete
@staff_member_required()
def product_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Product, slug=slug)
        object.delete()
        return redirect('ProjectDesign:product-list-page')
    else:
        object = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectDesign/Product/e-product-delete-page.html'
    context = {
        'title': 'Product Delete',
        'object': object,
    }
    return render(request, template_name, context)


# About Model (LCRUD)
# About List
@staff_member_required()
def about_list_view(request):
    objects_list = About.objects.all()

    template_name = 'ProjectDesign/About/a-about-list-page.html'
    context = {
        'title': 'About List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# About Create
@staff_member_required()
def about_create_view(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:about-list-page')
    else:
        form = AboutForm()

    template_name = 'ProjectDesign/About/b-about-create-page.html'
    context = {
        'title': 'About Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# About Retrieve
@staff_member_required()
def about_retrieve_view(request, slug):
    object = get_object_or_404(About, slug=slug)

    template_name = 'ProjectDesign/About/c-about-retrieve-page.html'
    context = {
        'title': 'About Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# About Update
@staff_member_required()
def about_update_view(request, slug):
    object = get_object_or_404(About, slug=slug)

    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:about-list-page')
    else:
        form = AboutForm(instance=object)

    template_name = 'ProjectDesign/About/d-about-update-page.html'
    context = {
        'title': 'About Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# About Delete
@staff_member_required()
def about_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(About, slug=slug)
        object.delete()
        return redirect('ProjectDesign:about-list-page')
    else:
        object = get_object_or_404(About, slug=slug)

    template_name = 'ProjectDesign/About/e-about-delete-page.html'
    context = {
        'title': 'About Delete',
        'object': object,
    }
    return render(request, template_name, context)
