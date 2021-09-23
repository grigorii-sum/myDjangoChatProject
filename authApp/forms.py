from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Textarea, Select, CheckboxInput, TextInput
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2"
        ]
