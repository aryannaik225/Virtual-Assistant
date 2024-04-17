import datetime
import sys
import os
import random
from time import sleep
import webbrowser
from bs4 import BeautifulSoup
import pyautogui
import pyttsx3
import requests
import speech_recognition
import plyer
from pygame import mixer
from plyer import notification
from speedtest import Speedtest
import tkinter as tk
from tkinter import scrolledtext
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QHBoxLayout
from PySide6 import QtCore 
from PySide6.QtGui import QFont, QTextCursor
import pyjokes

# from INTRO import play_gif
# play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 550) #speed of the bot speaking

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   
        r.energy_threshold = 150    #can take sound of energy 300
        audio = r.listen(source,0,5)  #will wait for 5 secs for you to speak

    try: 
        print("Understanding..")
        query = r.recognize_google(audio, language = 'en-IN')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def open_window():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.setWindowTitle("Jarvis: AI Assistant")
        self.setGeometry(1150, 390, 750, 650)

        self.setStyleSheet("""
            QMainWindow {
                background-image: url('bg.jpg');
            }
            QPushButton {
                background-color: #323643;
                border: 1px solid #323643; 
                border-radius: 10px; 
                color: white; 
                font-weight: bold;
                font-size: 24px;  
            }    
            QTextEdit {
                background-color: transparent; 
                border:none;           
            } 
        """)

        # Create a button and set its properties
        # self.button = QPushButton("Listen")
        # self.button.setFixedSize(200, 50)  # Set fixed size for the button
        # self.button.clicked.connect(self.recognize_speech) 

        # Create a text edit widget to display spoken text
        self.spoken_text_edit = QTextEdit()
        self.spoken_text_edit.setReadOnly(True)
        # self.spoken_text_edit.setAlignment(QtCore.Qt.AlignRight) 
         
        font = QFont()
        font.setPointSize(20)  # Set the font size to 20
        self.spoken_text_edit.setFont(font)

        # Create a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.spoken_text_edit)
        # layout.addWidget(self.button)

        # Set the central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def recognize_speech(self):
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 1
            recognizer.energy_threshold = 150   #can take sound of energy 300
            audio = recognizer.listen(source,0,5)   #will wait for 5 secs for you to speak

        try:
            print("Understanding..")
            query = recognizer.recognize_google(audio, language = 'en-IN', show_all=False)
            print(f"You Said: {query}\n")
            recognized_sentence_with_punctuation = query.capitalize() + '.'

            # Display the spoken text in the text edit widget
            self.spoken_text_edit.insertHtml("<br><div style='text-align: right;'>" +recognized_sentence_with_punctuation + "</div>")
            return query
        
        except Exception as e:
            print("Say that again")
            return "None"  
    
    def response_text(self,response):
            self.spoken_text_edit.insertHtml("<br><div style='text-align: left;'>" + response + "</div>") 
            cursor = self.spoken_text_edit.textCursor()
            cursor.movePosition(QTextCursor.End)  # Use QTextCursor directly
            self.spoken_text_edit.setTextCursor(cursor)

if __name__ == "__main__":
    while True:
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        icecream = MainWindow()
        icecream.show()
        query = icecream.recognize_speech().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            icecream.response_text(greetMe())

            while True:
                query = icecream.recognize_speech().lower()
                if "go to sleep" in query:
                    response = "Ok sir, you can call me anytime"
                    icecream.response_text(response)
                    speak("Ok sir, you can call me anytime")
                    break

                elif "hello" in query:
                    response = "Hello sir"
                    icecream.response_text(response)
                    speak("Hello sir")
                elif "how are you" in query:
                    response = "I'm absolutely perfect"
                    icecream.response_text(response)
                    speak("I'm absolutely perfect")
                elif "funny" in query:
                    response = pyjokes.get_joke()
                    icecream.response_text(response)
                    speak(response)
                elif "joke" in query:
                    response = pyjokes.get_joke()
                    icecream.response_text(response)
                    speak(response)
                elif "jokes" in query:
                    response = pyjokes.get_joke()
                    icecream.response_text(response)
                    speak(response)
                elif "thank you" in query:
                    response = "Welcome Sir"
                    icecream.response_text(response)
                    speak("Welcome sir")
                elif "thank" in query:
                    response = "Welcome sir"
                    icecream.response_text(response)
                    speak("Welcome sir")   
                elif "thanks" in query:
                    response = "Welcome sir"
                    icecream.response_text(response)
                    speak("Welcome sir")      

                elif "focus mode" in query:
                    response = "Are you sure that you want to enter focus mode:- [1 for YES / 2 for NO]"
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] "))
                    if (a==1):
                        response = "Entering the focus mode...."
                        icecream.response_text(response)
                        speak("Entering the focus mode....")
                        os.startfile("FocusMode.py")
                        exit()
                    else:
                        pass    

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()    

                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")     

                # elif "internet speed" in query:
                #     from speedtest import Speedtest
                #     wifi = Speedtest()
                #     upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                #     download_net = wifi.download()/1048576
                #     print("Wifi Upload Speed is", upload_net)
                #     print("Wifi download speed is ",download_net)
                #     speak(f"Wifi download speed is {download_net}")
                #     speak(f"Wifi Upload speed is {upload_net}")
                    
                elif "internet speed" in query:
                    try:
                        print("Calculating")
                        speak("Calculating")
                        wifi = Speedtest()
                        wifi.get_best_server()
                        download_speed = wifi.download() / 1024 / 1024  # Convert to Mbps
                        upload_speed = wifi.upload() / 1024 / 1024  # Convert to Mbps
                        icecream.response_text("Download Speed: {:.2f} Mbps".format(download_speed))
                        icecream.response_text("Upload Speed: {:.2f} Mbps".format(upload_speed))
                        print("Download Speed: {:.2f} Mbps".format(download_speed))
                        print("Upload Speed: {:.2f} Mbps".format(upload_speed))
                        speak("Wifi download speed is {:.2f} megabits per second".format(download_speed))
                        speak("Wifi upload speed is {:.2f} megabits per second".format(upload_speed))
                    except Exception as e:
                        icecream.response_text("An error occurred during the speed test: ", e)
                        print("An error occurred during the speed test:", e)
                        speak("Sorry, I couldn't perform the speed test at the moment.")

                elif "play a game" in query:
                    # from game import game_play
                    # game_play() 
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


                elif "tired" in query:
                    response = "Playing your favourite songs"
                    icecream.response_text(response)
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/HZsRjrYW-lk?si=HC1JbeBryPwG3mIh")
                        sleep(5)
                        pyautogui.press("f")
                    elif b==2:
                        webbrowser.open("https://youtu.be/jCEdTq3j-0U?si=vSU0Rzu_d-ZVw46r")
                        sleep(5)
                        pyautogui.press("f")
                    elif b==3:
                        webbrowser.open("https://youtu.be/II2EO3Nw4m0?si=LceJckFBQjWUxwlN")
                        sleep(5)
                        pyautogui.press("f") 
                     
            
                elif "pause" in query:
                    pyautogui.press("k")
                    response = "Video Paused"
                    icecream.response_text(response)
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    response = "Video Played"
                    icecream.response_text(response)
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    response = "Video muted"
                    icecream.response_text(response)
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    response = "Video Unmuted"
                    icecream.response_text(response)
                    speak("video unmuted")
                elif "full screen" in query:
                    response = "Full Screen toggled"
                    icecream.response_text(response)
                    pyautogui.press("f")
                    

                elif "volume up" in query:
                    from keyboard import volumeup
                    response = "Turning volume up"
                    icecream.response_text(response)
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    response = "Turning volume down"
                    icecream.response_text(response)
                    speak("Turning volume down, sir")
                    volumedown()   

                elif "open" in query:
                    from Dictapp import openappweb
                    response = f"Launching {query}, sir"
                    icecream.response_text(response)
                    openappweb(query)
                elif "launch" in query:
                    from Dictapp import openappweb
                    response = f"Launching {query}, sir"
                    icecream.response_text(response)
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    response = "Closing,sir"
                    icecream.response_text(response)
                    closeappweb(query)
                
                elif "google" in query:
                    from SearchNow import searchGoogle
                    response = searchGoogle(query)
                    icecream.response_text(response)
                    speak(response)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    response = searchWikipedia(query)
                    icecream.response_text(response)
                    speak(response)

                elif "temperature" in query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    response = f"current{search} is {temp}"
                    icecream.response_text(response)
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    response = f"current{search} is {temp}"
                    icecream.response_text(response)
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    response = "Set the time"
                    icecream.response_text(response)
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    response = "Alarm set"
                    icecream.response_text(response)
                    speak("Alarm set sir")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    response =  f"Sir, the time is {strTime}"
                    icecream.response_text(response)  
                    speak(f"Sir, the time is {strTime}")

                elif "finally sleep" in query:
                    response = "Going to sleep"
                    icecream.response_text(response)
                    speak("Going to sleep,sir")
                    # sys.exit(app.exec())
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    icecream.response_text(rememberMessage)
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    icecream.response_text(remember.read())
                    speak("You told me to " + remember.read())
                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    response = str(Calc(query))
                    icecream.response_text(response)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                    
                elif "ipl score" in query:
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup

                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")

                    try:
                        team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                        team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                        team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                        team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

                        print(f"{team1} : {team1_score}")
                        print(f"{team2} : {team2_score}")

                        notification.notify(
                            title="IPL SCORE",
                            message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                            timeout=15
                        )
                    except IndexError:
                        print("Error: Unable to retrieve IPL scores. Please try again later.")
                        notification.notify(
                            title="IPL SCORE",
                            message="Unable to retrieve scores. Please try again later.",
                            timeout=15
                        )

                elif "screenshot" in query:
                     im = pyautogui.screenshot()
                     response = "Screenshot taken"
                     icecream.response_text(response)
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "translate" in query:
                    # from SearchNow import searchGoogle
                    # # from Translator import translategl
                    # # query = query.replace("jarvis","")
                    # # query = query.replace("translate","")
                    # # translategl(query)
                    # searchGoogle(query)
                    # Extract the term to translate and the target language
                    from SearchNow import searchGoogle
                    to_translate = query.split("translate")[1].strip()  # Get the text to translate
                    target_language = query.split("in")[1].strip()  # Get the target language
                    
                    # Perform the translation using a web search
                    translation_query = f"translate {to_translate} in {target_language}"
                    searchGoogle(translation_query)


                