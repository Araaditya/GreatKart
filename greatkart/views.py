from django.shortcuts import render
from store.models import Product
# #superuser password GREATKART and username aaditya
# Email: test@gmail.com
# Username: superuseradmin1
# First name: aaditya
# Last name: thakar
# Password: GREATKART
# Password (again):
# def home(request):
#     return render(request, 'home.html')

def index(request):
    products = Product.objects.all().filter(is_available = True)
    context = {
        'products' : products
    }
    return render(request, 'index.html', context)