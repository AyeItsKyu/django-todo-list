from django import forms
from django.forms import DateInput, ModelForm
from .models import Task
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class TaskForm(ModelForm):
    complete_dt = forms.DateField(
    required=False,
    input_formats=['%d-%m-%Y'],
    widget=forms.TextInput(
        attrs={
            'placeholder': 'DD-MM-YYYY',
            'id' : 'complete_dt',
            'class' : 'form-control'
            }
        )
    )
    
    class Meta:
        model = Task
        fields = ["name","description","is_completed","complete_dt"]
        labels = {
            "name" : "Task name:",
            "description" : "Description:",
            "is_completed" : "Completed:",
            "complete_dt" : "Complete date:",
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control '}),
            'description' : forms.TextInput(attrs={'class' : 'form-control'}),
            'is_completed' : forms.CheckboxInput(attrs={'class' : 'form-check-input'})
        }

