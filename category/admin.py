from django.contrib import admin
from .models import Category

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_name',)}
    list_display = ('cat_name','slug')

admin.site.register(Category, categoryAdmin)