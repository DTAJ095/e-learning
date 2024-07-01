from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = [
            'bio',
            'photo_p',
            'type_p'
        ]
