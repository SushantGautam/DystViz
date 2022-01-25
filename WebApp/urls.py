from django.contrib import admin
from django.urls import path

from WebApp import views

urlpatterns = [
    path('', views.Graph.as_view(), name='Graph'),
    path('demo', views.demo, name='demo'),
    path('PlotSingleMP4Json/<str:mp4JsonFolderName>', views.PlotSingleMP4Json, name='PlotSingleMP4Json'),
]
