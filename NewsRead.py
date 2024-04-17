import requests
import json
import pyttsx3
from Jarvis_main import *

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)
icecream = MainWindow()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  
def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cd08a28883dd43d788a005f3b56d5d86",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cd08a28883dd43d788a005f3b56d5d86",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cd08a28883dd43d788a005f3b56d5d86",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cd08a28883dd43d788a005f3b56d5d86",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cd08a28883dd43d788a005f3b56d5d86",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cd08a28883dd43d788a005f3b56d5d86"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    icecream.response_text("Say field news that you want:")
    field = icecream.recognize_speech()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value 
            icecream.response_text(url)
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True: 
        icecream.response_text("url not found")
        print("url not found") 
        return

    news = requests.get(url).text
    news = json.loads(news) 
    icecream.response_text("Here is the first news.")
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"] 
        icecream.response_text(article)
        print(article)
        speak(article)
        news_url = articles["url"] 
        icecream.response_text(f"for more info visit: {news_url}")
        print(f"for more info visit: {news_url}")

        icecream.response_text("Do you want to continue?") 
        speak("Do you want to continue?")
        a = icecream.recognize_speech().lower()
        if str(a) == "yes":
            pass
        elif str(a) == "no":
            break
        else: 
            break        

    icecream.response_text("thats all")    
    speak("thats all")
