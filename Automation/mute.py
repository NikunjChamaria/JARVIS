import pyautogui as ui
from Head.Mouth import speak

def mute():
    speak("Volume muted")
    ui.press("volumemute")