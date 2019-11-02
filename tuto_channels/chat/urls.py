from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),

]