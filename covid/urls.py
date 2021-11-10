
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.covid , name = 'covid'),
]