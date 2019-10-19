from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    path(
        '',
        views.StoreCreateView.as_view(),
        name='list'),
    path(
        'create/',
        views.StoreCreateView.as_view(),
        name='create'),
    path(
        '<pk>/details/',
        views.StoreDetailView.as_view(),
        name='details'),
    path(
        '<pk>/delete/',
        views.StoreDeleteView.as_view(),
        name='delete'),
]
