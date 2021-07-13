from django.db import models
from django.contrib.auth.models import User

# from django.db.models.base import Model
# from django.shortcuts import reverse

# Create your models here.
class Customer(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='User' )
    first_name = models.CharField(blank=False, null=False, max_length=60)
    middle_name = models.CharField(blank=False, null=False, max_length=60)
    last_name = models.CharField(blank=False, null=False, max_length=60)
    email = models.EmailField()

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def get_product_cat(self):
        return self.name.capitalize()

    def __str__(self):
        return self.name.capitalize()


class Product(models.Model):
    # product_cat_id = models.ForeignKey(ProductCategory, related_name='prod_cat_id', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    Time_record = models.DateTimeField(auto_now_add=True)
    agent_id = models.ForeignKey(User, related_name='agent', on_delete=models.CASCADE)
    product_img1 = models.ImageField( verbose_name='Product Image 1', upload_to='uploads/products')
    product_img2 = models.ImageField( verbose_name='Product Image 2', upload_to='uploads/products')
    # product_img3 = models.ImageField( blank=True, null=True,verbose_name='Product Image 3', upload_to='uploads/products')
    prize = models.DecimalField(max_digits=10000, decimal_places=2)
    product_description = models.TextField(blank=True, null=True)

    

    def __str__(self):
        return self.product_name
    
    def __str__(self):
        return self.product_description

    def img_url1(self):
        if self.product_img1.url:
            return self.product_img1.url
        else:
            return '/static/website/images/img_1.jpg'
    
    def img_url2(self):
        if self.product_img2.url:
            return self.product_img2.url
        else:
            return '/static/website/images/img_1.jpg'

    def img_url3(self):
        if self.product_img3.url:
            return self.product_img3.url
        else:
            return '/static/website/images/img_1.jpg'


class latestProduct(models.Model):
    latest_product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    Time_record = models.DateTimeField(auto_now_add=True)
    latest_product_img = models.ImageField( verbose_name='latest Product Image 1', upload_to='uploads/products')
    agent_id = models.ForeignKey(User, related_name='latest_property_agent', on_delete=models.CASCADE)
    latest_prize = models.DecimalField(max_digits=10000, decimal_places=2)
    latest_product_description = models.TextField(blank=True, null=True)
    latest_product_cat_id = models.ForeignKey(ProductCategory, related_name='lat_property_cat', on_delete=models.CASCADE)
    # name = models.CharField(max_length=200)

    def __str__(self):
        return self.latest_product_name
    
    def __str__(self):
        return self.latest_product_description

    def latest_img_url1(self):
        if self.latest_product_img.url:
            return self.latest_product_img.url
        else:
            return '/static/website/images/img_1.jpg'
    



class featureProduct(models.Model):
    feature_product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    Time_record = models.DateTimeField(auto_now_add=True)
    feature_product_img = models.ImageField( verbose_name='Feature Product Image 1', upload_to='uploads/feature product_img')
    agent_id = models.ForeignKey(User, related_name='feature_product_agent', on_delete=models.CASCADE)
    prize = models.DecimalField(max_digits=10000, decimal_places=2)
    feature_product_description = models.TextField(blank=True, null=True)
    feature_product_cat_id = models.ForeignKey(ProductCategory, related_name='feature_product_cat_id', on_delete=models.CASCADE)
    


    def __str__(self):
        return self.feature_product_name
    
    def __str__(self):
        return self.feature_product_description

    def feat_img_url1(self):
        if self.feature_product_img.url:
            return self.feature_product_img.url
        else:
            return '/static/website/images/img_1.jpg'

class carousel_slide(models.Model):
    carousel_product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    Time_record = models.DateTimeField(auto_now_add=True)
    carousel_product_img = models.ImageField( verbose_name='carousel Product Image 1', upload_to='uploads/carousel product_img')
    agent_id = models.ForeignKey(User, related_name='carousel_product_agent', on_delete=models.CASCADE)
    prize = models.DecimalField(max_digits=10000, decimal_places=2)
    carousel_product_description = models.TextField(blank=True, null=True)
    carousel_product_cat_id = models.ForeignKey(ProductCategory, related_name='carousel_product_cat_id', on_delete=models.CASCADE)
    # name = models.CharField(max_length=200)


    def __str__(self):
        return self.carousel_product_name
    
    def __str__(self):
        return self.carousel_product_description

    def feat_img_url1(self):
        if self.carousel_product_img.url:
            return self.carousel_product_img.url
        else:
            return '/static/website/images/img_1.jpg'

class ContactAgent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    agent_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
