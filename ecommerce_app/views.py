from django.shortcuts import render
from django.http import HttpResponse
from ecommerce_app.models import *

# Create your views here.
def home(request):
    featureprod = featureProduct.objects.order_by('-Time_record')
    latestprod = latestProduct.objects.order_by('-Time_record')[:4]
    pageadvert = {
        'homepage1':latestprod,
        'homepage2':featureprod
    }
    return render(request,'website/index.html',pageadvert)


def about(request):
    return render(request,'website/about.html')

def phones(request):
    all_phone = latestProduct.objects.filter(latest_product_cat_id__name='Phone')
    return render(request,'website/product-list1.html', {'AllPhones':all_phone})

def laptops(request):
    all_laptops = latestProduct.objects.filter(latest_product_cat_id__name='Laptop')
    return render(request,'website/product-list2.html', {'laptops':all_laptops})

def contact(request):
    return render(request,'website/contact.html')