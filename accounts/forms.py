from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Employee


class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Employee
        fields=['first_name','last_name','username','email','password1','password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Employee
        fields = ['username', 'password']
