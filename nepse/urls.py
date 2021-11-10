from django.urls import path, re_path
from . import views

urlpatterns = [
    
    path('', views.nepse, name='nepse'),
    #re_path(r'(P?<str:stockname>\D+)', views.nepse, name='stock'),
    #re_path(r'^<str:name>', views.nepse, name='nepse'),

]
