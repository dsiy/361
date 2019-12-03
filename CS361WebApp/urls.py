from django.urls import path
from . import views

urlpatterns = [
  path('', views.welcome, name='CS361WebApp-welcome'),
  path('home/', views.home, name='CS361WebApp-home'),
  path('coursetime/', views.coursetime, name='CS361WebApp-coursetime'),
]