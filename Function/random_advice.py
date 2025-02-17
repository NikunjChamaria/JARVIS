import requests

from Head.Mouth import speak


def get_random_advice():
    res= requests.get("https://api.adviceslip.com/advice").json()
    speak(res['slip']['advice'])
    return res['slip']['advice']

