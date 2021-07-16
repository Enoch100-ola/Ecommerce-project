from django.shortcuts import render
from django.http import HttpResponse
from ecommerce_app.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    featureprod = latestProduct.objects.filter(latest_product_cat_id__name='Laptop')[:4]
    latestprod = latestProduct.objects.filter(latest_product_cat_id__name='Phone')[:4]
    pageadvert = {
        'homepage1':latestprod,
        'homepage2':featureprod
    }
    return render(request,'website/index.html',pageadvert)


def about(request):
    aboutme = Aboutpage.objects.all()
    return render(request,'website/about.html', {'abtme':aboutme})

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

def ProductDetail(request, slug):
    try:

        prod = latestProduct.objects.get(slug=slug)
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            print(name, email, phone)
            product = latestProduct.objects.get(slug=slug)
            agent = product.agent_id
            ContactAgent.objects.create(name=name, phone=phone, email=email, address=address, agent_id=agent )
            print('Success')
        return render(request,'website/product-detail.html', {'single_prod':prod})
    except ObjectDoesNotExist as error:
        print(f'You have this error {error}')
        return render(request, 'website/404.html')

def aboutDetail(request, abt_id):
    abt = Aboutpage.objects.get(id=abt_id)
    return render(request,'website/about-detail.html', {'single_abt':abt})