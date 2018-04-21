from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jarvis/', views.jarvis, name='jarvis'),
]