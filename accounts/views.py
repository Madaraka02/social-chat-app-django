import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


from .forms import *

# Create your views here.
def register(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'You are already auhtenticated as{user.email}')
    context={}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get('next')
            if destination:
                return redirect(destination)
            return redirect("home")    
        else: 
            context['registartion_form']  = form




    return render(request, 'accounts/register.html')    