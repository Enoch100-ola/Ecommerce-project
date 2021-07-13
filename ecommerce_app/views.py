from django.shortcuts import render
from django.http import HttpResponse
from ecommerce_app.models import *

# Create your views here.
def home(request):
    featureprod = latestProduct.objects.order_by('-Time_record')[:4:]
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
    no_of_AvaliablePhone = latestProduct.objects.filter(latest_product_cat_id__name='Phone').count()

    phon = {
        'AllPhones':all_phone,
        'NoPhoneAvaliable':no_of_AvaliablePhone
    }

    return render(request,'website/product-list1.html', phon)

def laptops(request):
    all_laptops = latestProduct.objects.filter(latest_product_cat_id__name='Laptop')
    NumAvaliable = latestProduct.objects.filter(latest_product_cat_id__name='Laptop').count()
    lap = {
        'laptops':all_laptops,
        'numOflaptop':NumAvaliable
    }
    return render(request,'website/product-list2.html', lap)

def contact(request):
    return render(request,'website/contact.html')

def ProductDetail(request, prod_id):
    prod = latestProduct.objects.get(id=prod_id)
    return render(request,'website/product-detail.html', {'single_prod':prod})