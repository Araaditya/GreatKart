from django.shortcuts import render
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
    return render(request, 'index.html')