import email
from pyexpat import model
from click import password_option
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255,help_text="Required field")
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)

        except Exception as e:
            return email
        raise forms.ValidationError('email is already taken')            

    def clean_email(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)

        except Exception as e:
            return username
        raise forms.ValidationError('username is already taken')      


class LoginForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model =  Account
        fields = ('email', 'password')


    def clean(self):
        if self.is_valid():
            # use name parameter in the email
            email = self.cleaned_data['email']  
            password = self.cleaned_data['password'] 

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login credentials")
