from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def jarvis(request):
    return HttpResponse(
        "<div align='center'><h1>Hello jarvis here!</h1></div>")
