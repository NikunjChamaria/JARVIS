import speech_recognition as sr 
import os
import threading
from colorama import Fore,Style,init
from googletrans import Translator

init(autoreset=True)

def print_loop():
        print(Fore.LIGHTGREEN_EX+ "I am Listening...",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)
        
async def Trans_hindi_to_english(text):
    if "play" in text:
        return text
    translator = Translator()
    detected_lang = await translator.detect(text)  
    detected_lang=detected_lang.lang
    if detected_lang != "en":
        translated =await translator.translate(text, src=detected_lang, dest="en")
    else:
        return text
    return translated.text

async def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold= False
    recognizer.energy_threshold= 35000
    recognizer.dynamic_energy_adjustment_damping = 0.03
    recognizer.dynamic_energy_ratio =1.9
    recognizer.pause_threshold =0.6
    recognizer.operation_timeout=None
    recognizer.non_speaking_duration=0.4
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.LIGHTGREEN_EX+ "I am Listening...",end="",flush=True)
        try:
            audio=recognizer.listen(source,timeout=None)
            print("\r"+Fore.LIGHTYELLOW_EX+"Got it, Recognizing..",end="",flush=True)
            recognized_txt= recognizer.recognize_google(audio).lower()
            if recognized_txt:
                translated_txt=await Trans_hindi_to_english(recognized_txt)
                print("\r"+Fore.BLUE+"Nikunj Chamaria: "+ translated_txt)
                return translated_txt
            else:
                return ""
        except sr.UnknownValueError:
                recognized_txt=""
        finally:
                print("\r",end="",flush=True)
            
        os.system("cls"  if os.name== "nt" else "clear")
            
        listen_thread = threading.Thread(target=listen)
        print_thread=threading.Thread(target=print_loop)
        listen_thread.start()
        print_thread.start()
        listen_thread.join()
        print_thread.join()    
            

