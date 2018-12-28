from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Signupform(UserCreationForm):
    username=forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': 'Username'})),
    first_name=forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name=forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email=forms.EmailField(help_text="Required, Inform a valid email address",widget=forms.TextInput(attrs={'placeholder': 'Email'}))
   # email_confirmed=forms.BooleanField(default=False)

    class meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')