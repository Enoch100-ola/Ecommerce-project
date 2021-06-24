from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from online_app import views


app_name = 'online_app'

urlpatterns = [
    path('', views.admin, name='admin'),
    path('login', views.login, name='login'),
    path('view_products', views.view_products, name='view_products'),

]