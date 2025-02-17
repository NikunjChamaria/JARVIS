import psutil
import time
from Head.Mouth import speak

def battery_alert():
    time.sleep(5)
    while True:
        battery=psutil.sensors_battery()
        percent=int(battery.percent)
        
        if percent<30:
            speak("sir, your device is running low on battery, pleae charge it")
        elif percent<10:
            speak("sir,this is the last chance, your battery is running very low")
        elif percent==100:
            speak("sir,battery is running on 100 percent full battery power, and i recommend you to unplug the charger if plugged")
        else:
            pass
        
        time.sleep(1500)

def battery_percentage():
    battery=psutil.sensors_battery()
    percent=int(battery.percent)
    
    speak(f"the device is running on {percent}% battery power")

def check_plugin_status():
    battery=psutil.sensors_battery()
    previous_state=battery.power_plugged
    
    while True:
        battery =psutil.sensors_battery()
        
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                speak("Plugging succesfully, your device is charging now")
            else:
                speak("Your deivce is plugged out, now you are running on your battery")
            
            previous_state=battery.power_plugged
        time.sleep(1)