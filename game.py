import pyttsx3
import speech_recognition as sr
import random
from Jarvis_main import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def game_play():
    icecream.response_text("Lets Play ROCK PAPkER SCISSORS !!")
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(Me_score<3 or Com_score<3):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = icecream.recognize_speech().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                icecream.response_text("ROCK")
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                icecream.response_text("PAPER")
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                icecream.response_text("SCISSORS")
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                icecream.response_text("ROCK")
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                icecream.response_text("PAPER")
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                icecream.response_text("SCISSORS")
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                icecream.response_text("ROCK")
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                icecream.response_text("PAPER")
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                icecream.response_text("SCISSORS")
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        response = f"Score:- ME :- {Me_score} : COM :- {Com_score}"
        icecream.response_text(response)
        i += 1

    response = f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}"
    icecream.response_text(response)
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")