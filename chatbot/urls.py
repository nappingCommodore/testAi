from django.urls import path

from . import views
from . import train

urlpatterns = [
    path('', views.home, name='home'),
    path(r'jarvis/', views.home, name='jarvis'),
    # path(r'train/', train.training, name='train')
]