from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            'first_name':forms.TextInput(attrs={"class": "form-control p-2"}),
            'email': forms.EmailInput(attrs={"class": "form-control p-2"}),
            'username': forms.TextInput(attrs={"class": "form-control p-2"})

        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter User name"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Password"}))

class PlaceOrderForm(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Enter Your Address"}))
    product=forms.CharField(max_length=120,widget=forms.TextInput(attrs={"class": "form-control"}))
