from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

list_to_train = [ 
                "hi",
                "hi there",
                "what's your name?",
                "i'm chatbot",
                "how old are you?",
                "i am ageless",
                "how are you?",
                "i am fine, thank you",
                "bye",
                "goodbye",
                "thank you",
                "you're welcome"
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)
