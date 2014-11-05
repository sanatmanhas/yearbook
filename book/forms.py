from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core import validators


class SignUpForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name  = forms.CharField(max_length=100)
	username   = forms.CharField(max_length=100)
	email	   = forms.EmailField()
	password   = forms.CharField(widget=forms.PasswordInput)
	conf_password = forms.CharField(widget=forms.PasswordInput)

