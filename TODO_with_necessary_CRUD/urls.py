from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.addTask, name='add-task'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('do-not-reload/', views.noReload, name='delete'),
]