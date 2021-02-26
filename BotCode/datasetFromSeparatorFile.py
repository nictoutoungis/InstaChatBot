#!/usr/bin/env python3

import random
import unicodedata
import re

textList  = list()
questions = list()
answers   = list()

def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
      if unicodedata.category(c) != 'Mn')


def preprocess_sentence(w):

    w = unicode_to_ascii(w.lower().strip())

    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)

    w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w)
    w = w.strip()

    w = '<start> ' + w + ' <end>'
    
    return w


def datasetFromSeparatorFile(textFile):

	print("-------------------------------------")

	textList = list()
	questions = list()
	answers = list()

	with open(textFile, 'r', encoding='iso-8859-1') as f:

		for line in f.readlines():

			_line = line.split(' +++$+++ ')
			text = _line[4]
			textList.append(text)

		print("Text list size: " + str(len(textList)))

		for i in range(0, len(textList)):
	    	
			if i % 2 == 0:

				questions.append(textList[i])

			else:

				answers.append(textList[i])

		pre_answers = [preprocess_sentence(w) for w in answers]
		strippedQuestions = [x.replace('\n', '') for x in questions]

		print("lenght of question set = " + str(len(strippedQuestions)))
		print("lenght of answer set = " + str(len(pre_answers)))

		return strippedQuestions, pre_answers