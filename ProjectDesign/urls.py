from django.urls import path
from .views import (
    entry_view,

    # Home Model
    home_list_view,
    home_create_view,
    home_retrieve_view,
    home_update_view,
    home_delete_view,

    # Category Model
    category_list_view,
    category_create_view,
    category_retrieve_view,
    category_update_view,
    category_delete_view,

    # Product Model
    product_list_view,
    product_create_view,
    product_retrieve_view,
    product_update_view,
    product_delete_view,

    # About Model
    about_list_view,
    about_create_view,
    about_retrieve_view,
    about_update_view,
    about_delete_view,

)


app_name = 'ProjectDesign'

urlpatterns = [
    # Entry
    path('', entry_view, name='entry-page'),

    # Home Model
    path('home-list-page/', home_list_view, name='home-list-page'),
    path('home-create-page/', home_create_view, name='home-create-page'),
    path('home-retrieve-page/<slug>/', home_retrieve_view, name='home-retrieve-page'),
    path('home-update-page/<slug>/', home_update_view, name='home-update-page'),
    path('home-delete-page/<slug>/', home_delete_view, name='home-delete-page'),

    # Category Model
    path('category-list-page/', category_list_view, name='category-list-page'),
    path('category-create-page/', category_create_view, name='category-create-page'),
    path('category-retrieve-page/<slug>/', category_retrieve_view, name='category-retrieve-page'),
    path('category-update-page/<slug>/', category_update_view, name='category-update-page'),
    path('category-delete-page/<slug>/', category_delete_view, name='category-delete-page'),

    # Product Model
    path('product-list-page/', product_list_view, name='product-list-page'),
    path('product-create-page/', product_create_view, name='product-create-page'),
    path('product-retrieve-page/<slug>/', product_retrieve_view, name='product-retrieve-page'),
    path('product-update-page/<slug>/', product_update_view, name='product-update-page'),
    path('product-delete-page/<slug>/', product_delete_view, name='product-delete-page'),

    # About Model
    path('about-list-page/', about_list_view, name='about-list-page'),
    path('about-create-page/', about_create_view, name='about-create-page'),
    path('about-retrieve-page/<slug>/', about_retrieve_view, name='about-retrieve-page'),
    path('about-update-page/<slug>/', about_update_view, name='about-update-page'),
    path('about-delete-page/<slug>/', about_delete_view, name='about-delete-page'),

]