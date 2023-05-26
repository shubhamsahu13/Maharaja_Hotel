from django.contrib import admin
from .models import (
    Home,
    Category,
    Product,
    About,
    Chef,
    Contact
)


admin.site.register(Home)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Chef)
admin.site.register(Contact)

