from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    pro_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    desc = models.TextField(max_length=300)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/categories/', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.pro_name