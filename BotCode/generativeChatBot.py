#!/usr/bin/env python3

import os
from tensorflow.keras import preprocessing
import numpy as np
import tokenizeData
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def main():

	while True:

		request = input(">")
		response = generateBotResponse(request)
		print(response.replace(" end", "."))

tokenizer = tokenizeData.createTokenizer()

x, maxlen_questions = tokenizeData.maxlen_questions()
y, maxlen_answers = tokenizeData.maxlen_answers()

def str_to_tokens( sentence : str ):
    
    words = sentence.lower().split()
    tokens_list = list()
    
    for word in words:
        
        tokens_list.append(tokenizer.word_index[word]) 
    
    return preprocessing.sequence.pad_sequences([tokens_list] , maxlen=maxlen_questions , padding='post')


enc_model = load_model("models/generative_chat_encoder_model.h5", compile=False)
dec_model = load_model("models/generative_chat_decoder_model.h5", compile=False)

def generateBotResponse(request):

	try: 

		states_values = enc_model.predict( str_to_tokens(request))
		empty_target_seq = np.zeros((1 , 1))
		empty_target_seq[0, 0] = tokenizer.word_index['start']
		stop_condition = False
		decoded_translation = ''

		while not stop_condition :
			dec_outputs , h , c = dec_model.predict([ empty_target_seq ] + states_values )
			sampled_word_index = np.argmax(dec_outputs[0, -1, :])
			sampled_word = None

			for word , index in tokenizer.word_index.items() :
	            
				if sampled_word_index == index :
	                
					decoded_translation += ' {}'.format(word)
					sampled_word = word
	        
			if sampled_word == 'end' or len(decoded_translation.split()) > maxlen_answers:
	            
				stop_condition = True
	            
			empty_target_seq = np.zeros( ( 1 , 1 ) )  
			empty_target_seq[ 0 , 0 ] = sampled_word_index
			states_values = [ h , c ]

		return decoded_translation

	except KeyError:


		errorMessage = "Sorry I don't know one of the words in this sentence, my data set is quite small as of now"
		
		return errorMessage
		
		pass

if __name__ == "__main__":

	main()
