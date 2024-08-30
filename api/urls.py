from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('services/',views.services, name='services'),
    path('login/',views.login, name='login')
]
