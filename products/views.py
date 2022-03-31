from django.shortcuts import render, redirect
from .models import Product
from .import forms


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('products:list') 
    else:
        form = forms.CreateProduct()
    return render(request, 'product_create.html', {'form':form})

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
   
class ProductUpdate(UpdateView):
    model = Product
    fields = ['category', 'title', 'description', 'price', 'quantity', 'sku', 'picture']
    success_url = reverse_lazy('products:list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')