from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms

class CreerUtilisateur(UserCreationForm):
    class Meta:
       model=User
       filds=['username','email','password1','password2']
