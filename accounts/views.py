from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CustomAuthenticationForm,EmployeeCreationForm
from django.contrib.auth.models import User
from .models import Employee
# Create your views here.


class UserCreateView(CreateView):
    form_class=EmployeeCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('item:index')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'


class UserDetailView(LoginRequiredMixin,DetailView):
    model = Employee
    template_name = "accounts/profile.html"


class UserLogOutView(LogoutView):
    model = Employee
    template_name = 'accounts/logout.html'
