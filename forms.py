from django.db import models
from django.forms import ModelForm
from django import forms
from siteprofiles.models import *
from registration.forms import RegistrationForm
          
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        exclude = ('employer','address','user',)
  
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = ('professor','address','user',)
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('student','user','skills','address','study')