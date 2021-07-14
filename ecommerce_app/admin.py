from ecommerce_app import models
from django.contrib import admin
from ecommerce_app.models import *
# from .models import *
admin.site.site_header='Ecommerce Website'
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(latestProduct)
class LeatestProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('latest_product_name',)}




admin.site.register(ProductCategory)
admin.site.register(ContactAgent)
admin.site.register(Customer)
admin.site.register(featureProduct)
admin.site.register(carousel_slide)
admin.site.register(Aboutpage)

