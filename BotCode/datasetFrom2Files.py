#!/usr/bin/env python3

import re
import random

def datasetFrom2Files(inputQuestionFile, inputAnswerFile):

	data_path = inputQuestionFile
	data_path2 = inputAnswerFile
	
	with open(data_path, 'r', encoding='utf-8') as f:
	  lines = f.read().split('\n')

	with open(data_path2, 'r', encoding='utf-8') as f:
	  lines2 = f.read().split('\n')

	lines = [re.sub(r"\[\w+\]",'hi',line) for line in lines]
	lines = [" ".join(re.findall(r"\w+",line)) for line in lines]

	lines2 = [re.sub(r"\[\w+\]",'',line) for line in lines2]
	lines2 = [" ".join(re.findall(r"\w+",line)) for line in lines2]

	pairs = list(zip(lines,lines2))

	questions = [i[0] for i in pairs]
	answers   = [i[1] for i in pairs]

	answers_with_tags = list()

	for i in range(len(answers)):
    
	    if type(answers[i]) == str:
	        answers_with_tags.append(answers[i])
	    else:
	        questions.pop(i)

	answers = list()
	
	for i in range(len(answers_with_tags)) :

		answers.append( '<START> ' + answers_with_tags[i] + ' <END>' )

	return questions, answers