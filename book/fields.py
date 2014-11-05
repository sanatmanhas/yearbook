from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class PasswordField(forms.CharField):
	def pass_conf(self):
		data = super(SignUpForm, self).clear()
		passwd = cleaned_data.get("password")
		conf = cleaned_data.get("conf_password")
		if conf != passwd:
			raise forms.ValidationError('Both passwords should match')
