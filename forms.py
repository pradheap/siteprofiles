from django.forms import ModelForm
from django import forms
from siteprofiles.models import *
          
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        
class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        exclude = ('employer','address','user',)
  
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = ('professor','address','user',)
   
class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        exclude = ('address',)
        
class StudentForm(forms.ModelForm):
    dob = forms.DateField(('%d/%m/%Y',), label='Date of Birth', required=False,  
        widget=forms.DateTimeInput(format='%d/%m/%Y', attrs={
            'class':'input',
            'readonly':'readonly',
            'size':'15'
        })
    )
    class Meta:
        model = Student
        exclude = ('student','user','skills','address','study')