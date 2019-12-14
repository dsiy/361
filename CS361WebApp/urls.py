from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='CS361WebApp-welcome'),
    path('home/', views.home, name='CS361WebApp-home'),
    path('coursetime/', views.coursetime, name='CS361WebApp-coursetime'),
    path('assign/', views.assign, name='CS361WebApp-assign'),
    path('classList/', views.classlist, name='CS361WebApp-classList'),
    path('priority/', views.priority, name='CS361WebApp-priority'),
]
