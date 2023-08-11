from .models import CRUD
from django import forms

class MakeForm(forms.ModelForm):
    class Meta:
        model=CRUD
        fields=['user','text']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)