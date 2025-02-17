import threading
import random
import time
import asyncio
from Function.welcome import *
from Function.wish import wish
from Head.brain import brain
from Head.Ear import listen
from Data.dlg_data.dlg import *
from Automation.open import open
from Automation.close import close
from Automation.minimise import minimise
from Automation.maximise import maximise
from Automation.increase_volume import increase_volume
from Automation.decrease_volume import decrease_volume
from Automation.mute import mute
from Automation.take_screenshot import take_screenshot
from Function.check_online_offline import is_online
from Function.random_advice import get_random_advice
from Friday.Fspeak import fspeak
from Function.battery import *
from Function.play_music import play_on_youtube
from Function.send_whatsapp import send_whatsapp_message

shutdown_event = threading.Event()  

def cmd():
    wish()
    while not shutdown_event.is_set():
        text = asyncio.run(listen())
        text = text.lower()

        if text in wake_up_jarvis:
            welcome()
        elif text in bye_jarvis:
            bye()
            shutdown_event.set()
            break
        elif "jarvis" in text:
            text = text.replace("jarvis", "")
            if "open" in text:
                open(text)
            elif "close" in text:
                close()
            elif "send a message" in text:
                send_whatsapp_message(text)
            elif "play" in text:
                play_on_youtube(text)
            elif "minimise" in text or "minimize" in text:
                minimise()
            elif "maximize" in text or "maximise" in text:
                maximise()
            elif "volume up" in text:
                increase_volume()
            elif "volume down" in text:
                decrease_volume()
            elif "mute" in text:
                mute()
            elif "take a screenshot" in text:
                take_screenshot()
            elif "check battery percent" in text:
                battery_percentage()
            else:
                brain(text)

def advice():
    while not shutdown_event.is_set():
        x = random.choice([500, 523, 855, 84, 30, 34, 42, 622, 646, 23])
        
        time.sleep(x) 

        if shutdown_event.is_set():
            break  

        speak("I have some suggestions for you, sir.")

        text = asyncio.run(listen())
        text = text.lower()

        if "yes" in text:
            get_random_advice()
        else:
            speak("No problem, sir.")

def jarvis():
    task1 = threading.Thread(target=cmd)
    #task2 = threading.Thread(target=advice)
    #task3 = threading.Thread(target=battery_alert)
    #task4 = threading.Thread(target=check_plugin_status)

    task1.start()
    #task2.start()
    #task3.start()
    #task4.start()

    task1.join()
    #task2.join()
    #task3.join()
    #task4.join()

def check_jarvis():
    if is_online():
        random_online = random.choice(system_online_messages)
        fspeak(random_online)
        jarvis() 
    else:
        random_offline = random.choice(system_offline_messages)
        fspeak(random_offline)

check_jarvis()
