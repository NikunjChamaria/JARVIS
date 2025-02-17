import os
import re
import sys
import threading
import requests
import wikipedia
import faiss
import numpy as np
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Head.Mouth import speak

load_dotenv()

QA_FILE_PATH = os.getenv("DATASET_PATH")

def load_qa_data(file_path):
    qa_dict = {}
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":", 1)
                if len(parts) == 2:
                    q, a = parts
                    qa_dict[q.lower().strip()] = a.strip()
    return qa_dict

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    return ' '.join([word for word in tokens if word.isalnum() and word not in stop_words])

def train_tfidf(questions):
    if not questions:
        return None, None
    vectorizer = TfidfVectorizer(preprocessor=preprocess_text)
    X = vectorizer.fit_transform(questions)
    return vectorizer, X

def train_word2vec(questions):
    tokenized_questions = [word_tokenize(q) for q in questions if q.strip()]
    if not tokenized_questions:
        return None
    return Word2Vec(sentences=tokenized_questions, vector_size=100, window=5, min_count=1, workers=4)

def sentence_vector(sentence, model):
    if model is None:
        return np.zeros((100,))
    words = word_tokenize(sentence)
    valid_words = [word for word in words if word in model.wv]
    if not valid_words:
        return np.zeros((model.vector_size,))
    return np.mean([model.wv[word] for word in valid_words], axis=0)

def build_faiss_index(vectors):
    if vectors.shape[0] == 0:
        return None
    d = vectors.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(vectors)
    return index

def search_best_match(query, vectorizer, tfidf_X, word2vec_model, faiss_index, dataset_questions, threshold=0.4):
    if not dataset_questions:
        return None

    query_tfidf = vectorizer.transform([query]) if vectorizer else None
    similarities = (query_tfidf @ tfidf_X.T).toarray()[0] if query_tfidf is not None else []

    query_vec = sentence_vector(query, word2vec_model).reshape(1, -1) if word2vec_model else None
    D, I = faiss_index.search(query_vec, 1) if faiss_index and query_vec is not None else (None, None)
    
    faiss_match_idx = I[0][0] if D is not None and D[0][0] < threshold else -1
    tfidf_match_idx = similarities.argmax() if similarities else -1
    
    if similarities and similarities[tfidf_match_idx] >= threshold:
        return dataset_questions[tfidf_match_idx]
    elif faiss_match_idx != -1:
        return dataset_questions[faiss_match_idx]

    return None

def save_qa_data(file_path, new_question, new_answer):
    existing_data = load_qa_data(file_path)
    new_question = new_question.lower().strip()
    existing_data[new_question] = new_answer
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in existing_data.items():
            f.write(f"{q}:{a}\n")

def wiki_search(prompt):
    search_prompt = re.sub(r'\bjarvis\b|\bwikipedia\b|\bsearch\b', '', prompt, flags=re.I).strip()
    try:
        search_results = wikipedia.search(search_prompt)
        if not search_results:
            google_search(prompt)
            return
        wiki_summary = wikipedia.summary(search_results[0], sentences=2)
        speak(wiki_summary)
        save_qa_data(QA_FILE_PATH, search_prompt, wiki_summary)
    except wikipedia.exceptions.DisambiguationError:
        google_search(prompt)
    except wikipedia.exceptions.PageError:
        google_search(prompt)

API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

def google_search(query):
    query = re.sub(r"who is |what is ", "", query, flags=re.I).strip()
    
    if query:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CSE_ID}"
        try:
            response = requests.get(url)
            search_results = response.json()

            if 'items' in search_results:
                top_result = search_results['items'][0]
                snippet = top_result['snippet']
                
                google_response = snippet
                
                save_qa_data(QA_FILE_PATH, query, google_response)
                speak(google_response)
            else:
                speak("I couldn't find any relevant results on Google.")
        except Exception as e:
            speak(f"An error occurred while searching Google: {str(e)}")
    else:
        speak("I did not catch what you said.")

def preprocess_question(question):
    prefixes = ['who is ', 'what is ', 'who was ', 'what was ', 'tell me about ', 'give me information on ']
    question = question.lower().strip()
    for prefix in prefixes:
        if question.startswith(prefix):
            return question[len(prefix):].strip()
    return question


def is_math_question(question):
    math_symbols = [
        '+', '-', '*', '/', '^', '**', 'sqrt', 'square root', 'mod', 'factorial', '%', 
        'sum', 'difference', 'product', 'times', 'divided by', 'equals', '=', 'is', 
        'greater than', 'less than', 'greater than or equal to', 'less than or equal to',
        'sin', 'cos', 'tan', 'cot', 'sec', 'cosec', 'log', 'ln', 'absolute value',
        'pi', 'e', 'x', 'y', 'z', 'parenthesis', '(', ')', 'multiply', 'plus', 'minus'
    ]
    if any(symbol in question.lower() for symbol in math_symbols):
        return True
    return False

def evaluate_math_question(question):
    if is_math_question(question):
        try:
            clean_question = re.sub(r'[^0-9+\-*/^().]', '', question)
            
            if not clean_question:
                return ""

            result = eval(clean_question)
            return result
        except SyntaxError:
            return ""
        except Exception as e:
            return ""
    else:
        return ""

def brain(text):
    try:
        math_response = evaluate_math_question(text)
        if math_response != "":
            speak_thread = threading.Thread(target=speak, args=(str(math_response),))
            speak_thread.start()
            speak_thread.join()
            return

        text = preprocess_question(text) 
        dataset = load_qa_data(QA_FILE_PATH)

        if text in dataset:
            response = dataset[text]
        else:
            dataset_questions = list(dataset.keys())
            if not dataset_questions:
                wiki_search(text)
                return

            vectorizer, tfidf_X = train_tfidf(dataset_questions)
            word2vec_model = train_word2vec(dataset_questions)
            w2v_vectors = np.array([sentence_vector(q, word2vec_model) for q in dataset_questions]) if word2vec_model else np.empty((0, 100))
            faiss_index = build_faiss_index(w2v_vectors)

            best_match = search_best_match(text, vectorizer, tfidf_X, word2vec_model, faiss_index, dataset_questions)
            response = dataset.get(best_match, None)

        if response:
            speak_thread = threading.Thread(target=speak, args=(response,))
            speak_thread.start()
            speak_thread.join()
        else:
            wiki_search(text)

    except Exception as e:
        wiki_search(text)



