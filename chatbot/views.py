from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime

from django.views.decorators.csrf import csrf_protect




message = ["Hello, how are you?"]
# userOrBot = "bot"

@csrf_protect
def home(request):
    if request.method == 'POST':
        msg = request.POST.get("msg")
        message.append(msg)
        userOrBot = "you"
        return render(request, 'home.html', {'message': message},{'userOrBot': userOrBot})
    else:
        # t = get_template('home.html')
        # message = ["hi betty", "this is jarvis", "good to go", "hasta la vista"]
        # html = t.render({'message': message})
        userOrBot = "bot"
        return render(request, 'home.html', {'message': message},{'userOrBot': userOrBot})
