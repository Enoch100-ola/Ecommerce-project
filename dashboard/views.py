from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return HttpResponse('login_view')

def register(request):
    return HttpResponse('register')

def dashboards(request):
    return HttpResponse('dashboards')

def profile(request):
    return HttpResponse('profile')

# Create your views here.
