from django import forms
from django.contrib.auth.models import User
from .models import ProfileModel


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['image',]
