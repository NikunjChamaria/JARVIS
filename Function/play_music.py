import pywhatkit
from Head.Mouth import speak

def play_on_youtube(text):
    text=text.replace("play","")
    text=text.strip()
    pywhatkit.playonyt(text)
    speak(f"playing {text}")