from django import forms

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=255)


    class Meta:
        model = User
        fields = [ "password"]
        widgets ={
            "password" : forms.PasswordInput()
        }

      