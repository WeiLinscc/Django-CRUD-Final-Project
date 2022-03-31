from django import forms
from .import models

class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['category', 'title', 'description', 'price', 'quantity', 'sku', 'picture']

class EditProduct(forms.ModelForm):
        model = models.Product
        fields = ['category', 'title', 'description', 'price', 'quantity', 'sku', 'picture']