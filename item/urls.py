from django.urls import path
from . import views

app_name="item"
urlpatterns = [
    path('', views.ListAndCreate.as_view(), name='index'),
    path('create/', views.ListAndCreate.as_view(), name='create'),
    path('delete-item/<pk>', views.ItemDeleteView.as_view(), name='delete'),
    path('item/<pk>', views.ListAndDetail.as_view(), name='details'),
    path('search/?query=', views.ItemSearchView.as_view(), name='search')
]
