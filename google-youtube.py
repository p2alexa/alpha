#!/usr/bin/env python3

import speech_recognition as sr
import urllib
import urllib.parse
import webbrowser
import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import os

r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Do you want to search something on google or play a video on youtube?")
  os.system("espeak 'Do you want to search something on google or play a video on youtube?'")
  audio = r.listen(source)
  
try:

	print("google thinks you said:" +r.recognize_google(audio))
	x=r.recognize_google(audio)
	if 'YouTube' in x:
		print("What you want to play on youtube?")
		os.system("espeak 'What you want to play on youtube?'")
		r = sr.Recognizer()

		with sr.Microphone() as source:
  			r.adjust_for_ambient_noise(source)  # here
  			audio = r.listen(source)
  
		try:

			print("google thinks you said:" +r.recognize_google(audio))
			y=r.recognize_google(audio)
		
			textToSearch=y
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
	if 'Google' in x:
		print("What you want to search on Google?")
		os.system("espeak 'What you want to search on Google?'")
		r = sr.Recognizer()

		with sr.Microphone() as source:
  			r.adjust_for_ambient_noise(source)  # here
  			audio = r.listen(source)
  
		try:

			print("google thinks you said:" +r.recognize_google(audio))
			z=r.recognize_google(audio)
			#final_data=z.strip()
			#done_data=final_data.split()
			#for i in done_data:
			webbrowser.open_new_tab('https://www.google.com/search?q='+z)
		except:
			print("Google Speech Recognition could not understand audio")
			pass
except:
	print("Google Speech Recognition could not understand audio")
	pass

