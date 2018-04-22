from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<html><title>Jarvis</title></html>")


def jarvis(request):
    return HttpResponse(
        "<div align='center'><h1>Hello jarvis here!</h1></div>")
