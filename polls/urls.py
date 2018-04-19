from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('loggedout/', views.loggedout, name='loggedout'),
    path('weather/', views.weather, name='weather'),
    path('weatherhandle/', views.weatherhandle, name="weatherhandle"),
    path('notes/', views.notes, name="notes"),
    path('notes/modifynote/<int:noteId>', views.modifyNote, name="modifyNote"),
    path('notes/deletenote/<int:noteId>', views.deleteNote, name="deletenote"),
    path('graph/<str:graphType>', views.createGraph, name="createGraph"),
    path('graph/city/<str:cityName>', views.cityList, name="cityList")

]
