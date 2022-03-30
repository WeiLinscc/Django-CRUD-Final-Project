from dataclasses import field
from pyexpat import model
from django import forms
from .import models

class CreateCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['title']