import pyautogui as ui
from Head.Mouth import speak

def minimise():
    speak("minimizing")
    ui.hotkey("win","down")