from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('data/', views.data, name='data'),
    path('service1/', views.service1, name='service1'),
    path('service2/', views.service2, name='service2'),
]

