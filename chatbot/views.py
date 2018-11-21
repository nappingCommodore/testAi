from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
import random
import sqlite3
from chatterbot.trainers import ListTrainer

from django.views.decorators.csrf import csrf_protect

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

message = ["Hello, My name is Jarvis. How may I help you?"]
botMsg = ["Hello how are you?", "My name is Jarvis.", "Weather is good today.", "What do you do?", "Okay", "Hmm", "Ohh", "What do you do?"
            "nice to meet you.", "What is your name?", "Good!!", "Fine", "I didn't get",
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."]
# userOrBot = "bot"

chatbot.set_trainer(ListTrainer)

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
        message.append(botReplied(msg))
        return render(request, 'home.html', {'message': message})
    else:
        # t = get_template('home.html')
        # message = ["hi betty", "this is jarvis", "good to go", "hasta la vista"]
        # html = t.render({'message': message})
        return render(request, 'home.html', {'message': message})
    conn.close()

def botReplied(msg):
    chatbot.train(botMsg)
    response = chatbot.get_response(msg)
    botMsg.append(response)
    # return botMsg[random.randint(0, len(botMsg)-1)]
    return response
