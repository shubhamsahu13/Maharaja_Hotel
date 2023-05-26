from django.urls import path
from .views import (
    home_view,
    product_retrieve_view
)

app_name = 'ProjectModel'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('product-retrieve-page/<slug:slug>/', product_retrieve_view, name='product-retrieve-page'),
]