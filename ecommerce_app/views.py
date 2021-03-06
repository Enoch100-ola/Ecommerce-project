from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ecommerce_app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from ecommerce_app.forms import *


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
    # try:

        prod = latestProduct.objects.get(slug=slug)
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            prod = latestProduct.objects.get(slug=slug)
            agent = prod.agent_id
            agent_email = prod.agent_id.email


            subject = 'Contact Agent Form'
            context = {
                        'name':name,
                        'email':email,
                        'phone':phone,
                        'address':address,
                        'agent':agent,
                    }
            html_message = render_to_string('website/mail-template.html', context)
            plain_message = strip_tags(html_message)
            from_email = settings.FROM_EMAIL
            send = mail.send_mail(subject, plain_message, from_email, [agent_email,], html_message=html_message)
            if send:
                ContactAgent.objects.create(name=name, phone=phone, email=email, address=address, agent_id=agent )
                messages.success(request, 'Message sent')
                print('Success')
            else:
                messages.error(request, 'Email not sent')
    
        return render(request,'website/product-detail.html', {'single_prod':prod})
    # except ObjectDoesNotExist as error:
        # print(f'You have this error {error}')
        # return render(request, 'website/404.html')

def aboutDetail(request, abt_id):
    abt = Aboutpage.objects.get(id=abt_id)
    return render(request,'website/about-detail.html', {'single_abt':abt})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('ecommerce_app:AdminPage')
            else:
                login(request, user)
                return redirect('ecommerce_app:ViewProduct')
        else:
            messages.error(request, 'username and password do not match')

    return render(request, 'backend_website/login.html')

@login_required(login_url='/ecommerce/login/')
def Admin_dashboard(request):
    return render(request, 'backend_website/admin.html')

def View_product(request):
    return render(request, 'backend_website/view-products.html')

def logout_view(request):
    logout(request)
    return redirect('ecommerce_app:login')

def cart(request):
    return render(request, 'website/cart.html')

def add_product(request):
    if request.method == 'POST':
        product_form = AddLatestProduct(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'New Product added successfully ')
    else:
        product_form = AddLatestProduct()
    return render(request, 'backend_website/add-product.html', {'proc':product_form})