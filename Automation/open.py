import random
import pyautogui as ui
import time
from Head.Mouth import speak
from Data.dlg_data.dlg import *
import webbrowser
import difflib

random_dlg=random.choice(open_dld)
random_open2=random.choice(open2)
random_sorry=random.choice(sorry_open)

def appopen(text):
    text=text.replace("open","")
    text=text.strip()
    speak(random_dlg+" "+ text)
    ui.press("win")
    time.sleep(0.5)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")

    
def webopen(text):
    text=text.replace("open","")
    text=text.replace("website","")
    text=text.replace("site","")
    text=text.strip()
    websites = {
    "google": "https://www.google.com/",
    "youtube": "https://www.youtube.com/",
    "facebook": "https://www.facebook.com/",
    "twitter": "https://www.twitter.com/",
    "instagram": "https://www.instagram.com/",
    "linkedin": "https://www.linkedin.com/",
    "wikipedia": "https://www.wikipedia.org/",
    "amazon": "https://www.amazon.com/",
    "ebay": "https://www.ebay.com/",
    "reddit": "https://www.reddit.com/",
    "netflix": "https://www.netflix.com/",
    "whatsapp": "https://web.whatsapp.com/",
    "tiktok": "https://www.tiktok.com/",
    "snapchat": "https://www.snapchat.com/",
    "pinterest": "https://www.pinterest.com/",
    "quora": "https://www.quora.com/",
    "github": "https://www.github.com/",
    "stackoverflow": "https://stackoverflow.com/",
    "microsoft": "https://www.microsoft.com/",
    "apple": "https://www.apple.com/",
    "yahoo": "https://www.yahoo.com/",
    "bing": "https://www.bing.com/",
    "duckduckgo": "https://www.duckduckgo.com/",
    "medium": "https://www.medium.com/",
    "spotify": "https://www.spotify.com/",
    "adobe": "https://www.adobe.com/",
    "cloudflare": "https://www.cloudflare.com/",
    "bbc": "https://www.bbc.com/",
    "cnn": "https://www.cnn.com/",
    "nytimes": "https://www.nytimes.com/",
    "forbes": "https://www.forbes.com/",
    "hulu": "https://www.hulu.com/",
    "zoom": "https://www.zoom.us/",
    "dropbox": "https://www.dropbox.com/",
    "salesforce": "https://www.salesforce.com/",
    "paypal": "https://www.paypal.com/",
    "telegram": "https://web.telegram.org/",
    "discord": "https://www.discord.com/",
    "walmart": "https://www.walmart.com/",
    "bestbuy": "https://www.bestbuy.com/",
    "aliexpress": "https://www.aliexpress.com/",
    "imdb": "https://www.imdb.com/",
    "cnbc": "https://www.cnbc.com/",
    "businessinsider": "https://www.businessinsider.com/",
    "nasa": "https://www.nasa.gov/",
    "espn": "https://www.espn.com/",
    "fandom": "https://www.fandom.com/",
    "twitch": "https://www.twitch.tv/",
    "coursera": "https://www.coursera.org/",
    "udemy": "https://www.udemy.com/"
    }
    
    website_name_lower=text.lower()
    
    if website_name_lower in websites:
        speak(random_dlg+" "+ text)
        url= websites[website_name_lower]
        webbrowser.open(url)

    else:
        matches= difflib.get_close_matches(website_name_lower,websites.keys(),n=1,cutoff=0.6)
        if matches:
            closest_match=matches[0]
            text=closest_match
            speak(random_open2 + " "+ random_dlg + " "+text)
            url=websites[closest_match]
            webbrowser.open(url)

        else:
            speak(random_sorry)


def open(text):
    if "website" in text or "site" in text:
        webopen(text)
    elif "app" in text or "application" in text:
        text=text.replace("app","")
        text=text.replace("application","")
        appopen(text)
    else:
        appopen(text)
        
