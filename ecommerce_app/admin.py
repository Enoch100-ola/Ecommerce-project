from ecommerce_app import models
from django.contrib import admin
from ecommerce_app.models import *
# from .models import *
admin.site.site_header='Ecommerce Website'
# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(ContactAgent)
admin.site.register(Customer)

@admin.register(Product)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
