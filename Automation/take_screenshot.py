import pyautogui as ui
from Head.Mouth import speak

def take_screenshot():
    speak("Taking screenshot")
    screenshot = ui.screenshot()
    screenshot.save("screenshot.png")