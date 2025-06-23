from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pro_name',)}
    list_display = ('pro_name','price', 'stock', 'category', 'modified_date', 'is_available')

admin.site.register(Product, ProductAdmin)