from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()

chatbot = ChatBot("Ron Obvious")

conversation = [
    "Bonjour",
    "Salut!",
    "Comment ça va ?",
    "ça roule ma poule",
    "ça fait plaisir à entendre",
    "Merci.",
    "De rien."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("Salut")
print(response)

response = chatbot.get_response("Comment ça va ?")
print(response)
