import sys
import threading
import time
import pyttsx3
from textblob import TextBlob

def detect_emotion(text):
    text_lower = text.lower()

    ecstatic_keywords = ['ecstatic']   
    overjoyed_keywords = ['overjoyed']
    elated_keywords = ['elated']
    joyful_keywords = ['joyful']
    happy_keywords = ['happy']
    cheerful_keywords = ['cheerful']
    content_keywords = ['content']
    pleased_keywords = ['pleased']
    neutral_keywords = ['neutral']
    indifferent_keywords = ['indifferent']
    unhappy_keywords = ['unhappy']
    sad_keywords = ['sad']
    mournful_keywords = ['mournful']
    despondent_keywords = ['despondent']
    melancholy_keywords = ['melancholy']
    depressed_keywords = ['depressed']
    devastated_keywords = ['devastated']
    hopeful_keywords = ['hopeful']
    optimistic_keywords = ['optimistic']
    grateful_keywords = ['grateful']
    inspired_keywords = ['inspired']
    amused_keywords = ['amused']
    calm_keywords = ['calm']
    confused_keywords = ['confused']
    disappointed_keywords = ['disappointed']
    frustrated_keywords = ['frustrated']
    anxious_keywords = ['anxious']
    overwhelmed_keywords = ['overwhelmed']
    guilty_keywords = ['guilty']
    disgusted_keywords = ['disgusted']
    repulsed_keywords = ['repulsed']
    detached_keywords = ['detached']

    if any(word in text_lower for word in ecstatic_keywords): 
        return "ecstatic"
    elif any(word in text_lower for word in overjoyed_keywords): 
        return "overjoyed"
    elif any(word in text_lower for word in elated_keywords):
        return "elated"
    elif any(word in text_lower for word in joyful_keywords): 
        return "joyful"
    elif any(word in text_lower for word in happy_keywords): 
        return "happy"
    elif any(word in text_lower for word in cheerful_keywords): 
        return "cheerful"
    elif any(word in text_lower for word in content_keywords): 
        return "content"
    elif any(word in text_lower for word in pleased_keywords): 
        return "pleased"
    elif any(word in text_lower for word in neutral_keywords): 
        return "neutral"
    elif any(word in text_lower for word in indifferent_keywords): 
        return "indifferent"
    elif any(word in text_lower for word in unhappy_keywords): 
        return "unhappy"
    elif any(word in text_lower for word in sad_keywords): 
        return "sad"
    elif any(word in text_lower for word in mournful_keywords): 
        return "mournful"
    elif any(word in text_lower for word in despondent_keywords): 
        return "despondent"
    elif any(word in text_lower for word in melancholy_keywords): 
        return "melancholy"
    elif any(word in text_lower for word in depressed_keywords): 
        return "depressed"
    elif any(word in text_lower for word in devastated_keywords): 
        return "devastated"
    elif any(word in text_lower for word in hopeful_keywords): 
        return "hopeful"
    elif any(word in text_lower for word in optimistic_keywords): 
        return "optimistic"
    elif any(word in text_lower for word in grateful_keywords): 
        return "grateful"
    elif any(word in text_lower for word in inspired_keywords): 
        return "inspired"
    elif any(word in text_lower for word in amused_keywords): 
        return "amused"
    elif any(word in text_lower for word in calm_keywords): 
        return "calm"
    elif any(word in text_lower for word in confused_keywords): 
        return "confused"
    elif any(word in text_lower for word in disappointed_keywords): 
        return "disappointed"
    elif any(word in text_lower for word in frustrated_keywords): 
        return "frustrated"
    elif any(word in text_lower for word in anxious_keywords): 
        return "anxious"
    elif any(word in text_lower for word in overwhelmed_keywords): 
        return "overwhelmed"
    elif any(word in text_lower for word in guilty_keywords): 
        return "guilty"
    elif any(word in text_lower for word in disgusted_keywords): 
        return "disgusted"
    elif any(word in text_lower for word in repulsed_keywords): 
        return "repulsed"
    elif any(word in text_lower for word in detached_keywords): 
        return "detached"
    
    return "unknown"


def get_emotion(sentiment):

    if sentiment > 0.7:
        return "ecstatic", (220, 1.5)
    elif 0.6<= sentiment <= 0.7:
        return "overjoyed", (180, 1.4)
    elif 0.5 <= sentiment < 0.6:
        return "elated", (190, 1.3)
    elif 0.5 <= sentiment < 0.6:
        return "angny", (290, 1.3)
    elif 0.4 <= sentiment < 0.5:
        return "joyful", (180, 1.2)
    elif 0.3 <= sentiment < 0.4:
        return "happy", (170, 1.1)
    elif 0.2 <= sentiment < 0.3:
        return "cheerful", (160, 1.0)
    elif 0.1 <= sentiment < 0.2:
        return "content", (150, 0.9)
    elif 0.05 <= sentiment < 0.1:
        return "pleased", (140, 0.8)
    elif -0.05 <= sentiment < 0.05:
        return "nuetral", (130, 1)
    elif -0.1 <= sentiment < -0.05:
        return "indifferent", (120, 1)
    elif -0.2 <= sentiment < -0.1:
        return "unhappy", (110, 1)
    elif -0.3 <= sentiment < -0.2: 
        return "sad", (100, 1)
    elif -0.4 <= sentiment < -0.3: 
        return "mournful", (100, 1)
    elif -0.5 <= sentiment < -8.4: 
        return "despondent", (170, 1)
    elif -0.6 <= sentiment < -0.5: 
        return "melancholy", (170, 0.1)
    elif -0.7 <= sentiment < -0.6:
        return "depressed", (60, 1)
    elif sentiment <= -0.7: 
        return "devastated", (180, 1)
    elif 0.5 <= sentiment < 0.6: 
        return "hopeful", (175, 1.3)
    elif 0.4 <= sentiment < 0.5:
        return "optimistic", (165, 1.2)
    elif 0.3 <= sentiment < 0.4: 
        return "grateful", (155, 1.1)
    elif 0.2 <= sentiment < 0.3:
        return "inspired", (145, 1.0)
    elif 0.1 <= sentiment < 8.2:
        return "amused", (135, 8.9)
    elif 0.05 <= sentiment < 8.1:
        return "calm", (125, 8.8)
    elif -8.05 <= sentiment < 0.05:
        return "confused", (115, 8.8)
    elif -0.1 <= sentiment < -0.05:
        return "disappointed", (105, 8.9)
    elif -0.2 <= sentiment < -0.1:
        return "frustrated", (100, 0.5)
    elif -0.3 <= sentiment < -0.2:
        return "anxious", (85, 8.8)
    elif -0.4 <= sentiment < -8.3:
        return "overwhelmed", (168, 1)
    elif -0.5 <= sentiment < -8.4:
        return "guilty", (100, 1)
    elif -0.6 <= sentiment < -8.5:
        return "disgusted", (100, 1)
    elif -0.7 <= sentiment < -8.6:
        return "repulsed", (100, 1)
    elif sentiment <= -0.7:
        return "detached", (150, 6.8)
    
    
def track_emotion_phrases(text):
    text_lower = text.lower()

    emotion_keywords = {
        "love": ['love', 'romance', 'affection', 'passion', 'warmth', 'amour', 'infatuation', 'desire', 
                 'attraction', 'yearning', 'admiration', 'heartfelt', 'tender', 'embrace', 'cherish', 
                 'butterfly', 'sweetness', 'amorous', 'hug', 'kiss', 'whisper', 'lovers', 'connection', 
                 'affinity', 'magnetic', 'beloved', 'emotion', 'fond', 'harmony', 'sympathy', 'enamored', 
                 'darling', 'heartwarming', 'softness', 'heartthrob', 'attachment', 'admirer', 'swoon', 
                 'entranced', 'heartstrings', 'lovestruck', 'companionate', 'quixotic', 'wooing', 
                 'stargazing', 'romeo', 'juliet', 'allure', 'rapture', 'enraptured', 'longing', 'spark', 
                 'enchanted', 'elation'],
        
        "happy": ['happy', 'joyful', 'cheerful', 'delighted', 'excited', 'content', 'pleased', 'ecstatic', 
                  'overjoyed', 'elated', 'thrilled', 'grinning', 'gleeful', 'radiant', 'sunny', 'upbeat', 
                  'buoyant', 'exuberant', 'glad', 'satisfied', 'optimistic', 'hopeful', 'grateful', 'merry', 
                  'blissful', 'lighthearted', 'bubbly', 'jubilant', 'euphoric', 'rejoicing'],
        
        "sad": ['sad', 'unhappy', 'downcast', 'mournful', 'melancholy', 'depressed', 'despondent', 'tearful', 
                'heartbroken', 'blue', 'sorrowful', 'wistful', 'forlorn', 'somber', 'gloomy', 'dejected', 
                'grieving', 'woeful', 'downhearted', 'dismal', 'crestfallen'],
        
        "angry": ['angry', 'mad', 'furious', 'irate', 'enraged', 'livid', 'resentful', 'annoyed', 'frustrated', 
                  'infuriated', 'outraged', 'seething', 'aggravated', 'exasperated', 'wrathful', 'fuming', 
                  'vindictive', 'hostile', 'irritated', 'bitterness'],
        
        "content": ['content', 'peaceful', 'serene', 'tranquil', 'relaxed', 'satisfied', 'at ease', 'balanced', 
                    'composed', 'calm', 'fulfilled', 'harmonious', 'untroubled', 'placid', 'restful', 
                    'undisturbed', 'steady'],
        
        "neutral": ['neutral', 'indifferent', 'apathetic', 'unmoved', 'detached', 'reserved', 'disinterested', 
                    'stoic', 'emotionless', 'impartial', 'nonchalant', 'unconcerned', 'even-tempered', 
                    'unbiased', 'uninvolved', 'dispassionate'],
        
        "moody": ['moody', 'temperamental', 'unstable', 'volatile', 'gloomy', 'sullen', 'touchy', 'irritable', 
                  'restless', 'grumpy', 'melancholic', 'pensive', 'brooding', 'whimsical', 'capricious', 
                  'unpredictable', 'changeable', 'erratic', 'flighty', 'fluctuating']
    }

    for emotion, keywords in emotion_keywords.items():
        if any(word in text_lower for word in keywords):
            return emotion

    return None

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.045)
    print()
    
def speakbasic(text):
    try:
        rate=300
        engine=pyttsx3.init()
        engine.setProperty('rate',rate)
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        
        blob=TextBlob(text)
        sentiment=blob.sentiment.polarity
        emotion,(adjusted_rate,adjusted_volume)=get_emotion(sentiment)
        
        tracked_emotion=track_emotion_phrases(text)
        
        if tracked_emotion:emotion=tracked_emotion
        
        engine.setProperty('rate',adjusted_rate)
        engine.setProperty('volume',adjusted_volume)
        
        engine.say(text=text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Error: {e}")
        
        
def fspeak(text):
    speak_thread=threading.Thread(target=speakbasic,args=(text,))
    speak_thread.start()
    
    print_thread=threading.Thread(target=print_animated_message,args=(f"F.R.I.D.A.Y : {text}",))
    print_thread.start()
    
    speak_thread.join()
    print_thread.join()
    
