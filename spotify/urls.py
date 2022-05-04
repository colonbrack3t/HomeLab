from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('change_device', views.change_device, name="change_device"),
    path('login', views.login, name="login"),
    path('access_token', views.get_access_token, name="access_token"),
    path('refresh_token', views.refresh_token, name="refresh_token"),
]