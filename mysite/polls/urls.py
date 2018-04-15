from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('loggedout/', views.loggedout, name='loggedout'),
    path('weather/', views.weather, name='weather'),
    path('weatherhandle/', views.weatherhandle, name="weatherhandle"),
]
