from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import *

from .models import AbUser

# Create your views here.

def home(request):
    return render(request,"dhumtanana/home.html",)


# User Registration
def user_registration(request):
    if request.method == "POST":
        form_data = Registration(request.POST)
        
        if form_data.is_valid():
            password =  form_data.cleaned_data["password"]
            data = {
                "first_name" : form_data.cleaned_data["First_name"],
                "last_name" : form_data.cleaned_data["Last_name"],
                "email" : form_data.cleaned_data["email"],
                "username" : form_data.cleaned_data["username"]
            }
            u = AbUser(**data)
            u.set_password(password)
            u.save()
            return HttpResponse("Registration Successful")

    else:
        form_data = Registration()
        context = {
            "form" : form_data,
        }
        return render(request, "dhumtanana/registration.html", context)


# User login
def user_login(request):
    if request.method == "POST":
        form_data = Login(request.POST)
        
        if form_data.is_valid():
            email = request.POST["email"]
            print(' data: ',  email)
            password = request.POST["password"]
            print(' password: ',  password)       
            user = authenticate(email=email, password=password)
            print('user: ', user)
    
            if user:
                login(request, user)
                user_data = AbUser.objects.get(id=user.id)
                print(user_data)
                return render(request, "dhumtanana/profile.html", {"user":user_data})

    else:
        form_data = Login()
    return render(request,"dhumtanana/login.html", {"form": form_data})

    
