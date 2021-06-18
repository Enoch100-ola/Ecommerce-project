from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def products(request):
    return render(request,'website/product.html')

def product_detail(request):
    return render(request,'website/product-detail.html')