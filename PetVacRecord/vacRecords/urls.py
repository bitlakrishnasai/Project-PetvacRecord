import include
from django.contrib import admin
from django.urls import path
from vacRecords import views


urlpatterns = [
    path('', views.index,name="home"),
    path('login', views.login,name="login"),
]
