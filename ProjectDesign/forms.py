from django import forms
from .models import (
    Home,
    Category,
    Product,
    About,
)

# Home Model
class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


# Category Model
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


# Product Model
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


# About Model
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


