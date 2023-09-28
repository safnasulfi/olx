from django import forms
from vehicles.models import *

class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=VehicleModels
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "model_name":forms.TextInput(attrs={"class":"form-control"}),
            "km_driven":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "contact":forms.TextInput(attrs={"class":"form-control"})
        }
        


class VehicleChangeForm(forms.ModelForm):
    class Meta:
        model=VehicleModels
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "model_name":forms.TextInput(attrs={"class":"form-control"}),
            "km_driven":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "contact":forms.TextInput(attrs={"class":"form-control"})
        }

from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }




class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))