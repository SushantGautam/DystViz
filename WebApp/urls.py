from django.contrib import admin
from django.urls import path

from WebApp import views

urlpatterns = [
    path('', views.Graph.as_view(), name='Graph'),
    path('list', views.list, name='list'),
    path('demo', views.demo, name='demo'),
    path('Profiling', views.Profiling, name='Profiling'),
    path('PlotSingleMP4Json/<str:mp4JsonFolderName>', views.PlotSingleMP4Json, name='PlotSingleMP4Json'),
]
