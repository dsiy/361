from django.urls import path

import user
from . import views



urlpatterns = [
    path('', views.welcome, name='CS361WebApp-welcome'),
    path('home/', views.home, name='CS361WebApp-home'),
    path('coursetime/', views.coursetime, name='CS361WebApp-coursetime'),
    path('assign/', views.assign, name='CS361WebApp-assign'),
    path('classList/', views.classlist, name='CS361WebApp-classList'),
    path('updateinfo/', user.views.updateinfo, name='CS361WebApp-updateinfo'),
]
