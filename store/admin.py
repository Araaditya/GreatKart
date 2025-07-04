from django.contrib import admin
from .models import Product,Variation,RevieRating,ProductGallery
import admin_thumbnails

# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pro_name',)}
    list_display = ('pro_name','price', 'stock', 'category', 'modified_date', 'is_available')
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category', 'variation_value')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(RevieRating)
admin.site.register(ProductGallery)