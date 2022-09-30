from dataclasses import field
from django import forms
from django.contrib.auth.models import User #need to import because User is not our created model but it is from django
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm): #we need to inherit UserCreationForm hence we pass it as a parameter
    email = forms.EmailField()

    class Meta: #Meta class is a class which will hold info. about Register Form class
        model = User #django knows that this form belongs to some model & hence we are specifying which model
        fields = ['username','email','password1','password2']