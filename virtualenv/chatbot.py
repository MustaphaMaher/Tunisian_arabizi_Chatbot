from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot_weather import WeatherLogicAdapter

from cleaner import clean_corpus
from weather import get_weather
from wikipediaprocess import search_wikipedia
from newsapi import NewsApiClient




newsapi = NewsApiClient(api_key="$NEWS_API_KEY")

#adding mathematical adapters for math operations to the achatbot
chatbot = ChatBot("Chatbot tounsi",logic_adapters=[   
       {'import_path': 'chatterbot.logic.MathematicalEvaluation',
        },
        {'import_path': 'chatterbot.logic.BestMatch',},
 #       {'import_path': 'myadapter.MyLogicAdapter',},
        ])

CORPUS_FILE2="chat2.txt"
CORPUS_FILE3="chat3.txt"
trainer = ListTrainer(chatbot)
cleaned_corpus2=clean_corpus(CORPUS_FILE2)
cleaned_corpus3=clean_corpus(CORPUS_FILE3)
trainer.train(cleaned_corpus2)
trainer.train(cleaned_corpus3)



exit_conditions = (":q", "quit", "exit")
while True:
    print("************************************************************\nbech tchouf ta9s mtaa bled ekteb : meteo fi + ville\nbech tchouf e5er a5bar ekteb  : a5bar aala + sujet\nbecht tchouf definition mtaa 7aja ekteb : wiki +Sujet\nbech to5rej ekteb quit wala exit\ntnajem taatini ne7seb zeda\n************************************************************")
    query = input("> ")
    #print(query)
    if query in exit_conditions:
        break
    elif query.startswith("meteo fi "):
        # Get the country name from the input
        country = query.replace("meteo fi ", "")
        # Get the weather for the country
        weather = get_weather(country)
        print(f"ta9s: {weather}")
    elif query.startswith("wiki "):
        topic=query.replace("wiki ","")
        wiki=search_wikipedia(topic)
        print(wiki)
    elif query.startswith("a5bar aala "):
        theme=query.replace("a5bar aala ","")
        top_headlines = newsapi.get_everything(q=theme, sort_by='relevancy',language='fr')
        for article in top_headlines['articles']:
            print(article['title'])


    else:
        print(f"🤖 {str(chatbot.get_response(query))}")
