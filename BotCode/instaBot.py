#!/usr/bin/env python3

import random
import re
import argparse
import getpass

from time     import sleep
from selenium import webdriver
from bs4      import BeautifulSoup
from argparse import RawTextHelpFormatter

from instaPageObjectPattern import *


description = """\033[1;32;40m 
 ______                   __             ____            __      
/\__  _\                 /\ \__         /\  _`\         /\ \__   
\/_/\ \/     ___     ____\ \ ,_\    __  \ \ \L\ \    ___\ \ ,_\  
   \ \ \   /' _ `\  /',__\\ \ \/  /'__`\ \ \  _ <'  / __`\ \ \/  
    \_\ \__/\ \/\ \/\__, `\\ \ \_/\ \L\.\_\ \ \L\ \/\ \L\ \ \ \_ 
    /\_____\ \_\ \_\/\____/ \ \__\ \__/.\_\\ \____/\ \____/\ \__\ 
    \/_____/\/_/\/_/\/___/   \/__/\/__/\/_/ \/___/  \/___/  \/__/
                                                                 
                                                                 
    	        AI generated Instagram messages                           
 \033[0m"""


argParser = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)

argParser.add_argument("username", help="Your instagram username")
argParser.add_argument("user",     help="User to send first message to")

argParser.add_argument("-t","--time", help="Amount of time between bot refresh and responses (in seconds) (default = 20s)", type=int)
argParser.add_argument("-v", "--verbose", help="Display information in the terminal", action="store_true")

args = argParser.parse_args()

password = getpass.getpass()

import botPrediction

browser = webdriver.Firefox()

def main():

	user = args.user

	if args.time == None:

		time = 20

	else:

		time = args.time

	loadInstagramMessages()
	
	conversationPage, messagePage = goToConversation(user)

	htmlSource = browser.page_source
	request, spanTags = getLastMessage(htmlSource)
	
	user = getUsernameOfLastMessage(spanTags)

	request = ""

	conversationPage.sendMessageTo(user, "Hello I am an AI")

	while True:

		if request == "Bye":

			break

		else:

			sleep(time)
			htmlSource = browser.page_source
			request, spanTags = getLastMessage(htmlSource)
			response = botPrediction.chatbot_response(request)
			conversationPage.sendMessageTo(user, response)
			user = getUsernameOfLastMessage(spanTags)

			if args.verbose == True:

				print("Responding to: " + request)
				print("Sending message to: " + user)
			
			# messagePage.openConversationWith(user)
			browser.implicitly_wait(5)


	sleep(5)

	browser.close()
			
def loadInstagramMessages():

	browser.implicitly_wait(5)

	homePage = LoginPage(browser)

	feedPage = homePage.login(args.username, password)

	sleep(7)

	feedPage.clearEntryMessage()

	messagePage = feedPage.goToMessages()

def goToConversation(user):

	browser.implicitly_wait(5)

	messagePage = MessagePage(browser)

	conversationPage = messagePage.openConversationWith(user)

	sleep(2)

	return conversationPage, messagePage


def getUsernameOfLastMessage(spanTags):

	lastUser = re.findall("((?<=alt=\")[^']*)", spanTags)

	return lastUser[-1]

def getLastMessage(pageHtml):

	soup = BeautifulSoup(pageHtml, 'html.parser')

	spanTags = soup.findAll("span")

	lastMessageContent = spanTags[-1].get_text()

	return lastMessageContent, str(spanTags)


if __name__ == "__main__":

	main()
