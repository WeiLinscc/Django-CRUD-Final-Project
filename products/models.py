from email.policy import default
from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    sku = models.CharField(max_length=50)
    picture = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.description[:20] + '...'