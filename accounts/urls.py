# Django
from django.urls import path
# Project
from . import views

app_name="accounts"
urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/<pk>', views.UserDetailView.as_view(), name='profile'),
]
