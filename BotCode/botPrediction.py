#!/usr/bin/env python3

import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import json
import random
import os
import numpy as np

from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
lemmatizer = WordNetLemmatizer()
model = load_model('conversation_model.h5')

conversations = json.loads(open('conversation.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


def main():

	print("Hello")

	while True:

		message = input(">")
		response = chatbot_response(message)
		print(response)


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    
    for s in sentence_words:
        
        for i,w in enumerate(words):
            
            if w == s: 
                bag[i] = 1
                
                if show_details:
                    print ("found in bag: %s" % w)
    
    return(np.array(bag))

def predict_class(sentence, model):

    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    
    for r in results:
        return_list.append({"conversation": classes[r[0]], "probability": str(r[1])})
    
    return return_list

def getResponse(ints, conversations_json):
    tag = ints[0]['conversation']
    list_of_conversations = conversations_json['conversations']
    for i in list_of_conversations:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, conversations)
    return res

if __name__ == "__main__":

	main()
