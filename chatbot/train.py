from chatterbot import ChatBot
from django.shortcuts import render

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

chatbot = ChatBot("Ron Obvious")

def training(request):
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    chatbot.train(
        "chatterbot.corpus.english"
    )
    return render(request, 'home.html')