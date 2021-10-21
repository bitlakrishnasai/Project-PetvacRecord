import include
from django.contrib import admin
from django.urls import path
from vacRecords import views


urlpatterns = [
    path('', views.login,name="login"),
    path('login.html',views.signUp,name="login"),
    path('index.html', views.index,name="home"),

    
]
