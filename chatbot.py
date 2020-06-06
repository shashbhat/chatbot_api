from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'ProBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Artha aatijji bvc, sama pater',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 

# Custom Training
training_data_bot_qus = open('training_data/bot_qus_data.txt').read().splitlines()
training_data_general = open('training_data/custom_data2.txt').read().splitlines()

training_data = training_data_bot_qus + training_data_general

trainer = ListTrainer(chatbot)
trainer.train(training_data)  

