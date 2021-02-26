#!/usr/bin/env python3

import os
import yaml

def datasetFromYMLFiles(directory):

	dir_path = directory
	files_list = os.listdir(dir_path + os.sep)

	questions = list()
	answers = list()

	for filepath in files_list:
	    stream = open( dir_path + os.sep + filepath , 'rb')
	    docs = yaml.safe_load(stream)
	    conversations = docs['conversations']
	    for con in conversations:
	        if len( con ) > 2 :
	            questions.append(con[0])
	            replies = con[ 1 : ]
	            ans = ''
	            for rep in replies:
	                ans += ' ' + rep
	            answers.append( ans )
	        elif len( con )> 1:
	            questions.append(con[0])
	            answers.append(con[1])

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