#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.core.exceptions import ValidationError
from .models import Localisation, Identite

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,  widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(required = True, label = 'Username', max_length = 32)
    email = forms.CharField(required = True, label = 'Email', max_length = 32)
    password = forms.CharField(required = True,label = 'Password', max_length = 32, widget = forms.PasswordInput())


class LocalisationForm(forms.ModelForm):
	
	class Meta:
		model = Localisation
		fields = '__all__'
	
	def clean_cimetiere(self):
		return self.cleaned_data['cimetiere'].lower()
	

class IdentiteForm(forms.ModelForm):
	class Meta:
		model = Identite
		fields = '__all__'
