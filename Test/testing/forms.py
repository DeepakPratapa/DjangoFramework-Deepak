from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#converting django models to a form

from django.contrib.auth.models import User

#using forms class
from django import forms
#to use widget (fields)
from django.forms.widgets import PasswordInput,TextInput

#modifying the Existing default UserCreation Form

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields =['username','email','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use. Please use a different one.")
        return email


#modifying the existing User Authentication

class LoginForm(AuthenticationForm):

    username=forms.CharField(widget=TextInput())
    
    password=forms.CharField(widget=PasswordInput())

    