from datetime import date
from Data.dlg_data.dlg import *
import datetime
from Head.Mouth import speak
import random

today = date.today()
formatted_date=today.strftime("%d %b %y")
nowx=datetime.datetime.now()




def wish():
    current_hour=nowx.hour
    if 5<= current_hour< 12:
        gd_dlg=random.choice(good_morningdlg)
        speak(gd_dlg)
    elif 12<=current_hour<17:
        gd_dlg=random.choice(good_afternoondlg)
        speak(gd_dlg)
    elif 17<=current_hour<21:
        gd_dlg=random.choice(good_eveningdlg)
        speak(gd_dlg)
    else:
        gd_dlg=random.choice(good_nightdlg)
        speak(gd_dlg)
        
