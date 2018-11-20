from django.urls import path

from . import views

urlpatterns = [
    path('still-harbor-56063.herokuapp.com/', views.home, name='home'),
    path(r'still-harbor-56063.herokuapp.com/jarvis/', views.home, name='jarvis'),
]