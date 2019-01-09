from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/' views.Add_item, name='add'),
    path('remove/' views.remove_item, name='remove'),
]
