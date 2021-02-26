#!/usr/bin/env python3

import os
from tensorflow.keras import layers , activations , models , preprocessing, utils
from gensim.models import Word2Vec
import numpy as np
import tensorflow as tf
import pickle
import re
from keras.models import load_model
import datasetFrom2Files
import datasetFromTabFile
import datasetFromSeparatorFile
import tokenizeData
from time import sleep

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

questions, answers = datasetFrom2Files.datasetFrom2Files("datasets/human_text.txt", "datasets/robot_text.txt")

tokenizer = tokenizeData.createTokenizer()
VOCAB_SIZE = len( tokenizer.word_index )+1

vocab=[]

for word in tokenizer.word_index:
    vocab.append(word)

def tokenize(sentences):
    tokens_list=[]
    vocabulary=[]
    for sentence in sentences:
        sentence = sentence.lower()
        sentence = re.sub( '^a-zA-Z',' ',sentence)
        tokens = sentence.split()
        vocabulary+=tokens
        tokens_list.append(tokens)
    return tokens_list,vocabulary

tokenized_questions, maxlen_questions = tokenizeData.maxlen_questions()
padded_questions = preprocessing.sequence.pad_sequences(tokenized_questions, maxlen=maxlen_questions, padding='post')
encoder_input_data = np.array(padded_questions)
print(encoder_input_data.shape, maxlen_questions)

tokenized_answers, maxlen_answers = tokenizeData.maxlen_answers()
padded_answers = preprocessing.sequence.pad_sequences(tokenized_answers, maxlen=maxlen_answers, padding='post')
decoder_input_data = np.array(padded_answers)
print(decoder_input_data.shape, maxlen_answers)

tokenized_answers = tokenizer.texts_to_sequences(answers)
for i in range(len(tokenized_answers)):
    tokenized_answers[i]=tokenized_answers[i][1:]
padded_answers = preprocessing.sequence.pad_sequences(tokenized_answers, maxlen=maxlen_answers, padding='post')
one_hot_answers = utils.to_categorical(padded_answers, VOCAB_SIZE)
decoder_output_data = np.array(one_hot_answers)
print(decoder_output_data.shape)


encoder_inputs = tf.keras.layers.Input(shape=(None , ))
encoder_embedding = tf.keras.layers.Embedding(VOCAB_SIZE, 200 , mask_zero=True) (encoder_inputs)
encoder_outputs , state_h , state_c = tf.keras.layers.LSTM(200 , return_state=True)(encoder_embedding)
encoder_states = [ state_h , state_c ]

decoder_inputs = tf.keras.layers.Input(shape=( None ,  ))
decoder_embedding = tf.keras.layers.Embedding( VOCAB_SIZE, 200 , mask_zero=True) (decoder_inputs)
decoder_lstm = tf.keras.layers.LSTM( 200 , return_state=True , return_sequences=True)
decoder_outputs , _ , _ = decoder_lstm (decoder_embedding , initial_state=encoder_states)
decoder_dense = tf.keras.layers.Dense(VOCAB_SIZE , activation=tf.keras.activations.softmax) 
output = decoder_dense (decoder_outputs)

model = tf.keras.models.Model([encoder_inputs, decoder_inputs], output)
model.compile(optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit([encoder_input_data , decoder_input_data], decoder_output_data, batch_size=125, epochs=250) 
model.save('models/generative_chat_model.h5')

def make_inference_models():
    
    encoder_model = tf.keras.models.Model(encoder_inputs, encoder_states)
    
    decoder_state_input_h = tf.keras.layers.Input(shape=( 200 ,))
    decoder_state_input_c = tf.keras.layers.Input(shape=( 200 ,))
    
    decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
    
    decoder_outputs, state_h, state_c = decoder_lstm(
        decoder_embedding , initial_state=decoder_states_inputs)
    decoder_states = [state_h, state_c]
    decoder_outputs = decoder_dense(decoder_outputs)
    decoder_model = tf.keras.models.Model(
        [decoder_inputs] + decoder_states_inputs,
        [decoder_outputs] + decoder_states)

    encoder_model.save("models/generative_chat_encoder_model.h5")
    decoder_model.save("models/generative_chat_decoder_model.h5")

make_inference_models()