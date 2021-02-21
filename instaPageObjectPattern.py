#!/usr/bin/env python3

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class LoginPage:

	def __init__(self, browser):
		self.browser = browser
		self.browser.get('https://www.instagram.com/')

	def login(self, username, password):

		usernameInput = self.browser.find_element_by_css_selector("input[name='username']")
		passwordInput = self.browser.find_element_by_css_selector("input[name='password']")

		usernameInput.send_keys(username)
		passwordInput.send_keys(password)

		self.browser.find_element_by_xpath("//button[@type='submit']").click()

		return FeedPage(self.browser)


class FeedPage:

	def __init__(self, browser):
		self.browser = browser

	def clearEntryMessage(self):

		while True:
			
			try:
				
				self.browser.find_element_by_xpath("//button[text()='Not Now']").click()

				sleep(5)

			except NoSuchElementException:

				break

	def goToMessages(self):

		self.browser.find_element_by_class_name("xWeGp").click()
		sleep(2)

		return MessagePage(self.browser)

class MessagePage:
	
	def __init__(self, browser):
		self.browser = browser
		self.browser.get("https://www.instagram.com/direct/inbox/")

	def openConversationWith(self, user):

		conversationSelect = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div')
		self.browser.execute_script("arguments[0].click();", conversationSelect)
		sleep(2)

		self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
		sleep(2)

		self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div').click()
		sleep(2)

		self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div').click()
		sleep(2)

		return ConversationPage(self.browser)

class ConversationPage:

	def __init__(self, browser):
		self.browser = browser
	

	def sendMessageTo(self, user, message):

		self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
		sleep(2)

		self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
		sleep(2)



