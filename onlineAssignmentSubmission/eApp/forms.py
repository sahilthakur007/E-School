from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class TeacherProfileForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['firstname','lastname','email','password','mobile']