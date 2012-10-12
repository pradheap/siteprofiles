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
        exclude = ('employer','user',)
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('student','user','skills','address','study')
        
# This we don't need in case we are doing multi table inheritance rather than one-one       
#RegistrationForm.base_fields.update(UserProfileForm.base_fields)
#RegistrationForm.base_fields.update(StudentForm.base_fields)

#class CustomRegistrationForm(RegistrationForm):
    #first_name = forms.CharField(label="First Name:",help_text='')
    #last_name = forms.CharField(label="Last Name:",help_text='')
    #reg_no = forms.CharField(label="Reg No:",help_text='')
