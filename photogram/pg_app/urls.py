# This file contaign URLs for concrete app

from django.urls import path
from pg_app import views

urlpatterns = [
    path('', views.index, name='root'),
    path('index.html', views.index, name='index'),
]