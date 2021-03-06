import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout



from .forms import *

# Create your views here.
def register(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'You are already auhtenticated as{user.email}')
    context={}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request) 
            if destination:
                return redirect(destination)
            return redirect("home")    
        else: 
            context['registartion_form']  = form




    return render(request, 'accounts/register.html', context)    

def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request, *args, **kwargs):


    context={}
    user=request.user
    if user.is_authenticated:
        return redirect("home")

      
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request) 
                if destination:
                    return redirect(destination)
                return redirect("home") 
        else: 
            context['login_form']  = form
    return render(request,"accounts/login.html", context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect        