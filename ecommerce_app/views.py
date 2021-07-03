from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def phones(request):
    return render(request,'website/product-list1.html')

def laptops(request):
    return render(request,'website/product-list2.html')

def contact(request):
    return render(request,'website/contact.html')