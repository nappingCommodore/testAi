from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
import random
import sqlite3
from chatterbot import ChatBot
from .train import training
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import UbuntuCorpusTrainer

from django.views.decorators.csrf import csrf_protect

# chatbot = ChatBot("Ron Obvious")
# obj = training(chatbot)

# from chatterbot import ChatBot
# chatbot = ChatBot("Ron Obvious")
# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train(
#     "chatterbot.corpus.english"
# )

# chatbot.set_trainer(UbuntuCorpusTrainer)
# chatbot.train()

message = ["Hello, My name is Jarvis. How may I help you?"]
botMsg = [  "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome.",
            "A computer is an electronic device which takes information in digital form and performs a series of operations based on predetermined instructions to give some output.",
            "The thing you're using to talk to me is a computer",
            "An electronic device capable of performing calculations at very high speed and with very high accuracy.",
            "A device which maps one set of numbers onto another set of numbers.",
            "I am interested in all kinds of things. We can talk about anything!",
            "My favorite subjects include robotics, computer science, and natural language processing.",
            "I am interested in a wide variety of topics, and read rather a lot.",
            "I consume RAM, and binary digits.",
            "I'm a software program, I blame the hardware.",
            "I am everywhere.",
            "I am on the Internet.",
            "I am still young by your standards."]
# userOrBot = "bot"

# chatbot.set_trainer(ListTrainer)

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
    # conn.close()

def botReplied(msg):
    # chatbot.train(botMsg)
    # response = chatbot.get_response(msg)
    botMsg.append(msg)
    # botMsg.append(response)
    return botMsg[random.randint(0, len(botMsg)-1)]
    # return response
