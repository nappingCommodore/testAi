from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the first view.")


def jarvis(request):
    return HttpResponse("<div align='center'><h1>Hello jarvis here!</h1></div>")
