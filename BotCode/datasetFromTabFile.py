#!/usr/bin/env python3

import unicodedata
import re

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

def datasetFromTabFile(textFile):

	file = open(textFile,'r').read()

	qna_list = [f.split('\t') for f in file.split('\n')]

	questions = [x[0] for x in qna_list]
	answers = [x[1] for x in qna_list]

	pre_answers = [preprocess_sentence(w) for w in answers]

	print("lenght of question set = " + str(len(questions)))
	print("lenght of question set = " + str(len(answers)))

	return questions, pre_answers