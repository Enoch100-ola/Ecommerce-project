from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.shortcuts import reverse

# Create your models here.
class Customer(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='user' )
    first_name = models.CharField(blank=False, null=False, max_length=60)
    middle_name = models.CharField(blank=False, null=False, max_length=60)
    last_name = models.CharField(blank=False, null=False, max_length=60)
    email = models.EmailField()



class Product(models.Model):
    product_category_id = models.DecimalField(max_digits= 90, decimal_places=0)
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    Time_record = models.DateTimeField()
    product_img1 = models.ImageField(blank=True, null=True, verbose_name='Product Image 1', upload_to='uploads/products')
    product_img2 = models.ImageField(blank=True, null=True, verbose_name='Product Image 2', upload_to='uploads/products')
    product_img3 = models.ImageField( blank=True, null=True,verbose_name='Product Image 3', upload_to='uploads/products')
    prize = models.DecimalField(max_digits=9, decimal_places=2)
    product_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_name
    
    def __str__(self):
        return self.product_description

    def __str__(self):
        return self.product_img1



class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
class LatestProduct(models.Model):
    name = models.CharField(max_length=200)
    
    

