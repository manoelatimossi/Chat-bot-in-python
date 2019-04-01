from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot('bot',logic_adapters=[
        {
           'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.50
        }
   ]
)
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)
while True:
    user=input("You:  ")
    answer= bot.get_response(user)
    print("Rodolfo:",answer)
    
