from django import forms
from django.db.models import fields
from ecommerce_app.models import *


class AddLatestProduct(forms.ModelForm):
    productname = forms.CharField   

    class Meta():
        model = latestProduct
        fields = '__all__'

    def clean_name(self):
        caputured_product_name = self.cleaned_data.get('productname').capitalize()
        if latestProduct.objects.filter(latest_product_name=caputured_product_name).exists():
            raise forms.ValidationError(f'{caputured_product_name}) already exist')
        return caputured_product_name