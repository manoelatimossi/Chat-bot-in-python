from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
bot = ChatBot ('Avatar',logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])
conversation = ['Hi','Hello', 'How are you?', 'I am fine','How old are you?', '21 years old']
trainer= ListTrainer(bot)
trainer.train(conversation)
while True:
  question = input("You: ")
  answer = bot.get_response(question)
  print('Avatar: ',answer)
  
    
  
