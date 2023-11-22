from django.contrib import admin
from django.urls import path
from . import views

# URL을 변수로 사용 (app_name:name)
app_name = 'advertisement'

urlpatterns = [
    path('', views.index, name='index'),
    
    
]

