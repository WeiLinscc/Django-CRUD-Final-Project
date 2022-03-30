from urllib import request
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title