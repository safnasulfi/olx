from django.shortcuts import render,redirect
from django.views.generic import View
from vehicles.forms import *
from vehicles.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"registration.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs):
     form=LoginForm()
     return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("vehicle-list")
            else:
                return render(request,"login.html",{"form":form})
            


def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


class VehicleCreateView(View):
    def get(self,request,*args,**kwargs):
        form=VehicleCreateForm()
        return render(request,"create.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=VehicleCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("vehicle-list")
        else:
            return render(request,"create.html",{"form":form})
        

class VehicleListView(View):
    def get(self,request,*args,**kwargs):
        qs=VehicleModels.objects.all()
        return render(request,"list.html",{"vehicle":qs})
    

class VehicleUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=VehicleModels.objects.get(id=id)
        form=VehicleChangeForm(instance=obj)
        return render(request,"edit.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=VehicleModels.objects.get(id=id)
        form=VehicleChangeForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("vehicle-list")
        else:
            return render(request,"update.html",{"form":form})


class VehicleDeatileView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=VehicleModels.objects.get(id=id)
        return render(request,"deatiles.html",{"vehicle":qs})
    

class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=VehicleModels.objects.filter(id=id).delete()

        return redirect("vehicle-list")