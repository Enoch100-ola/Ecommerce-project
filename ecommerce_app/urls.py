from django.conf.urls import url	
from django.urls import path
from ecommerce_app import views

app_name = 'ecommerce_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('phones/',views.phones,name='phones'),
    path('laptops/',views.laptops,name='laptops'),
    path('<slug:slug>',views.ProductDetail,name='ProductDetail'),
    path('aboutdetail/<int:abt_id>',views.aboutDetail,name='AboutDetail'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('AdminPage/',views.Admin_dashboard,name='AdminPage'),
    path('ViewProduct/',views.View_product,name='ViewProduct'),
    path('Cart/',views.cart,name='cart'),
]