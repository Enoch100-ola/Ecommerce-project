from django import forms
from django.db.models import fields
from ecommerce_app.models import *


class AddLatestProduct(forms.ModelForm):
    productname = forms.CharField(
        label='Product Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Product Name'}
        ))   

    slug = forms.CharField(label='Slug',widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Put a hyphen for your slug name'}
        ))
     
    Time_record = forms.DateTimeField()

    agent_id = forms.DecimalField()

    product_img1 = forms.ImageField(label='Product image1', widget=forms.ClearableFileInput())

    product_img2 = forms.ImageField(label='Product image2', widget=forms.ClearableFileInput())
 
    prize = forms.DecimalField(label='Prize',widget=forms.NumberInput(
            attrs={'class': 'form-control', }
        ))
    product_description = forms.CharField(label='Product Description',widget=forms.Textarea(
            attrs={'class': 'form-control'}
        ))

    

    class Meta():
        model = latestProduct
        fields = '__all__'

    def clean_name(self):
        caputured_product_name = self.cleaned_data.get('productname').capitalize()
        if latestProduct.objects.filter(latest_product_name=caputured_product_name).exists():
            raise forms.ValidationError(f'{caputured_product_name}) already exist')
        return caputured_product_name