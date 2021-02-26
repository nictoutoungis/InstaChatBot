#!/usr/bin/env python3 

import os
import datasetFromTabFile
import datasetFrom2Files
import datasetFromSeparatorFile
from tensorflow.keras import preprocessing

questions, answers = datasetFrom2Files.datasetFrom2Files("datasets/human_text.txt", "datasets/robot_text.txt")

def createTokenizer():

    tokenizer = preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(questions + answers)

    return tokenizer

tokenizerGlobal = createTokenizer()


def maxlen_questions():

	tokenized_questions = tokenizerGlobal.texts_to_sequences(questions)
	maxlen_questions = max([len(x) for x in tokenized_questions])

	return tokenized_questions, maxlen_questions

def maxlen_answers():

	tokenized_answers = tokenizerGlobal.texts_to_sequences(answers)
	maxlen_answers = max([len(x) for x in tokenized_answers])

	return tokenized_answers, maxlen_answers