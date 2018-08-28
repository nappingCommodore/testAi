from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
import sqlite3

from django.views.decorators.csrf import csrf_protect

message = ["Hello, how are you?"]
# userOrBot = "bot"

@csrf_protect
def home(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    if request.method == 'POST':
        msg = request.POST.get("msg")
        insertVal = (msg, "you")
        try:
            cursor.execute("INSERT INTO chats(msg, who) VALUES(?, ?)", insertVal,)
            conn.commit()
        except Exception as e:
            print(e)
        
        message.append(msg)
        return render(request, 'home.html', {'message': message})
    else:
        # t = get_template('home.html')
        # message = ["hi betty", "this is jarvis", "good to go", "hasta la vista"]
        # html = t.render({'message': message})
        return render(request, 'home.html', {'message': message})
    conn.close()
