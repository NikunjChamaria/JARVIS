import pyautogui
import time

from Head.Mouth import speak


def send_whatsapp_message(command):

    if "send a message to" in command and "and say" in command:
        parts = command.split("and say")
        recipient_name = parts[0].replace("send a message to", "").strip()
        message = parts[1].strip()

        pyautogui.hotkey("win", "s") 
        time.sleep(0.5)
        pyautogui.write("WhatsApp")  
        time.sleep(0.5)
        pyautogui.press("enter")  
        time.sleep(2) 

        pyautogui.hotkey("ctrl", "f")
        time.sleep(0.5)
        pyautogui.write(recipient_name) 
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")  

        time.sleep(1)
        pyautogui.write(message)  
        time.sleep(0.5)
        pyautogui.press("enter")  

        speak(f"Message sent to {recipient_name}")


