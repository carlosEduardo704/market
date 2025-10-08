from django import forms
from products.models import Product


class ProductModelForm(forms.ModelForm):
    model = Product
    fields = '__all__'
