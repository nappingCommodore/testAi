from django.shortcuts import render

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

class training(object):
    def __init__(self, chatbot):
        chatbot.set_trainer(ChatterBotCorpusTrainer)
        chatbot.train(
            "chatterbot.corpus.english"
        )
    # return render(request, 'home.html')