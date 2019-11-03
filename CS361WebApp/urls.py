from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='CS361WebApp-home'),
  path('about/', views.about, name='CS361WebApp-about'),
]