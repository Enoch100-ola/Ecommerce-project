from django.conf.urls import url	
from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('register/',views.register,name='register'),
    path('dashboards/',views.dashboards,name='dashboards'),
    path('profile/',views.profile,name='profile'),
]