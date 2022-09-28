from distutils.command.build_scripts import first_line_re
from logging import PlaceHolder
from tkinter import Widget
from tkinter.ttk import Style
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class TeacherRegistrationForm(UserCreationForm):
	# first_name: forms.CharField(max_length=100,  widgets=forms.TextInput(
	# 	attrs={'class': 'form-control'}))
	# last_name: forms.CharField(max_length=100, widgets=forms.TextInput(
	# 	attrs={'class': 'form-control form-input'}))
	# email: forms.EmailField(widget=forms.EmailInput(
	# 	attrs={'class': 'form-control form-input'}))
	# username: forms.CharField(max_length=100, widget=forms.TextInput(
	# 	attrs={'class': 'form-control form-input'}))
	# password: forms.CharField(max_length=100, widget=forms.PasswordInput(
	# 	attrs={'class': 'form-control form-input'}))
    

	class Meta:
		model = User
		fields = ['first_name','last_name', 'username', 'email', 'password']
		widgets ={
			'first_name': forms.TextInput(attrs={'class': 'form-control form-input','placeholder':'firstname'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'lastname'}),
			'username': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'username'}),
			'email': forms.EmailInput(attrs={'class': 'form-control form-input', 'placeholder': 'email'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'password'}),
			
			
		}
		
	
        
		


class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'email', 'password', 'mobile']
