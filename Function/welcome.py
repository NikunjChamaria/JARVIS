from Data.dlg_data.dlg import *
from Head.Mouth import speak
import random

def welcome():
    welcom=random.choice(formal_greetings)
    speak(welcom)
    
def bye():
    bye_text=random.choice(jarvis_bye_messages)
    speak(bye_text)   