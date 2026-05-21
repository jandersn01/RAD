from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('singnup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]