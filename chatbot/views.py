from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    t = get_template('home.html')
    message = ["hi betty", "this is jarvis", "good to go", "hasta la vista"]
    html = t.render({'message': message})
    return HttpResponse(html)

def fillChat(request):
    return {
        "message": "Hello from the other side."
    }

def jarvis(request):
    now = datetime.datetime.now()
    return HttpResponse(
        "<div align='center'><h1>Hello, jarvis here!</h1> <p>Time now is %s</p></div>" % now)
