from django.urls import path
from . import views
from django.contrib import admin
from cadastro.views import cadastro_usuario

urlpatterns = [
    
    path('', views.cadastro_usuario, name='cadastro_usuario'),  
]
