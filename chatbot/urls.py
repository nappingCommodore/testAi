from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'jarvis/', views.home, name='jarvis'),
]