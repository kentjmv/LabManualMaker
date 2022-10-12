from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class SearchLab(ModelForm):
    class Meta:
        model = Lab_Manual
        fields = ['lab_name',
        'instructor',
        'course_code',
        'activity_name',
        ]
        

class NewLab(ModelForm):
    class Meta:
        model = Lab_Manual
        fields = '__all__'

        widgets = {
            'lab_name': forms.TextInput(attrs={'class':'myform'}),
            'instructor': forms.Select(attrs={'class':'myform'}),
            'course_code': forms.Select(attrs={'class':'myform'}),
            'activity_name': forms.TextInput(attrs={'class':'myform'}),
            'activity_no': forms.NumberInput(attrs={'class':'myform'}),
            
        }