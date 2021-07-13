from django.shortcuts import render
from django.http import HttpResponse
from ecommerce_app.models import *

# Create your views here.
def home(request):
    featureprod = featureProduct.objects.order_by('-Time_record')
    latestprod = latestProduct.objects.order_by('-Time_record')
    pageadvert = {
        'homepage1':latestprod,
        'homepage2':featureprod
    }
    return render(request,'website/index.html',pageadvert)


def about(request):
    return render(request,'website/about.html')

def phones(request):
    all_phone = Product.objects.all()
    return render(request,'website/product-list1.html', {'AllPhones':all_phone})

def laptops(request):
    return render(request,'website/product-list2.html')

def contact(request):
    return render(request,'website/contact.html')