from deep_translator import GoogleTranslator
from Jarvis_main import *
from Jarvis_main import MainWindow
from Jarvis_main import speak

icecream = MainWindow()

def Translationss(to_tranlate, target_language):
    translated = GoogleTranslator(source='auto', target=f'{target_language}').translate(to_tranlate)
    print(translated)
    icecream.response_text(f"{to_tranlate} in {target_language} is {translated}")
    speak(f"{to_tranlate} in {target_language} is {translated}")