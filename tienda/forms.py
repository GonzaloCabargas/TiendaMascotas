from dataclasses import field, fields
from xml.sax.xmlreader import AttributesImpl
from django import forms
from .models import Contacto, user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
class CustomUserCreationForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username',"email" ,"password1", "password2"]