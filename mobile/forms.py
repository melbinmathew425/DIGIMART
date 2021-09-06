from django import forms
from django.forms import ModelForm
from .models import Brand,Product

class BrandModelForm(ModelForm):
    class Meta:
        model=Brand
        fields=["brand_name"]

class ProductCreationForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "specs": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.Select(attrs={"class": "form-select"})
        }
    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price" )
        if price<500:
            msg="invalid price"
            self.add_error("price",msg)