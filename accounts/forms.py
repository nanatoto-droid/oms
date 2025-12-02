from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['start_date', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    