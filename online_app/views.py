from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admin(request):
    return render(request, 'backend_website/admin.html')

def login(request):
    return render(request, 'backend_website/login.html')

def view_products(request):
    return render(request, 'backend_website/view-products.html')