from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from myapp.models import audio


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password']

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Foydalanuvchi'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Parol'}),
        }
class audiocreate(ModelForm):
    class Meta:
        model = audio
        fields = '__all__'