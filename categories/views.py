from dataclasses import field
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Category
from .import forms

# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = forms.CreateCategory(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('categories:list') 
    else:
        form = forms.CreateCategory()
    return render(request, 'category_create.html', {'form':form})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
   
class CategoryUpdate(UpdateView):
    model = Category
    fields = ['title']
    success_url = reverse_lazy('categories:list')

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categories:list')