from django.urls import path
from . import views

urlpatterns = [
  path('', views.TAManager.as_view(), name='CS361WebApp-home'),
  path('about/', views.about, name='CS361WebApp-about'),
  path('classlist/', views.ClassList.get(), name='CS361WebApp-classlist')
]
