import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime
from datetime import *
from Sim_main import *

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

icecream = MainWindow()

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# def takeCommand():
#     r = speech_recognition.Recognizer()
#     with speech_recognition.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold = 1
#         r.energy_threshold = 150
#         audio = r.listen(source,0,4)

#     try:
#         print("Understanding..")
#         query  = r.recognize_google(audio,language='en-in')
#         print(f"You Said: {query}\n")
#     except Exception as e:
#         print("Say that again")
#         return "None"
#     return query

strTime = int(datetime.datetime.now().strftime("%H"))
update = int((datetime.datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    icecream.response_text("Who do you want to message?")
    speak("Who do you want to message")
    icecream.response_text("Aadit \nAryan")
    speak("Aadit or Aryan")
    icecream.response_text("Say first or second")
    speak("Say first or second")
    a = None
    while a == None:
        a = icecream.recognize_speech().lower()
    if a == "one" or a == "1" or "first" in a:
        icecream.response_text("Whats the message?")
        speak("Whats the message")
        message = icecream.recognize_speech()
        pywhatkit.sendwhatmsg("+919984624288",message,time_hour=strTime,time_min=update)
        icecream.response_text("Message will be sent in 2 mins")
        speak("Message will be sent in 2 mins")
        pyautogui.press("enter")
    elif a== "two" or a == "2" or "second" in a:
        icecream.response_text("Whats the message?")
        speak("Whats the message")
        message = icecream.recognize_speech()
        pywhatkit.sendwhatmsg("+918779067940",message,time_hour=strTime,time_min=update)
        icecream.response_text("Message will be sent in 2 mins")
        speak("Message will be sent in 2 mins")
        pyautogui.press("enter")
