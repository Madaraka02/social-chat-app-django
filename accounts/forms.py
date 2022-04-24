import email
from pyexpat import model
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