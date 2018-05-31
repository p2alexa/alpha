#!/usr/bin/env python3

import speech_recognition as sr
import urllib
import urllib.parse
import webbrowser
import urllib.request  as urllib2 
from bs4 import BeautifulSoup

r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Say something!")
  audio = r.listen(source)

try:

	print("google thinks you said:" +r.recognize_google(audio))
	textToSearch=r.recognize_google(audio)
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)

	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    		print ('https://www.youtube.com' + vid['href'])
    		webbrowser.open('https://www.youtube.com' + vid['href'])
    		break

except:
	print("Google Speech Recognition could not understand audio")
	pass

