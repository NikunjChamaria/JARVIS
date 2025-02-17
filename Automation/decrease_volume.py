import pyautogui as ui
from Head.Mouth import speak

def decrease_volume():
    speak("Decreasing Volume")
    ui.press("volumedown")
    ui.press("volumedown")
    ui.press("volumedown")
    ui.press("volumedown")
    ui.press("volumedown")
    ui.press("volumedown")