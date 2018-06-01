#!/usr/bin/env python3

#Test by trying vlc
from gtts import gTTS
import speech_recognition as sr
import os
'''
r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Do you want to install or remove an application or command?")
  os.system("espeak 'Do you want to install or remove an application or command?'")
  audio = r.listen(source)
'''


def install_pkg(text):
	try:
	
		print("alexa thinks you said:" +text) #test with vlc
		xyz=text

		if 'install' in xyz:
			print("Which application or command do you want to install?")
			os.system("espeak 'Which application or command do you want to install?'")
			r = sr.Recognizer()

			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)  # here
				audio = r.listen(source)
			text_t=r.recognize_google(audio)

			try:

				print("alexa thinks you said:" +text_t)
				app=text_t
				os.system('sudo apt install '+app.lower())
			except:
				print("alexa could not understand audio")
				pass
	
		if 'remove' in xyz:
			print("Which application or command do you want to remove?")
			os.system("espeak 'Which application or command do you want to remove?'")
			r = sr.Recognizer()

			with sr.Microphone() as source:
	  			r.adjust_for_ambient_noise(source)  # here
	  			audio = r.listen(source)
	  			text_t=r.recognize_google(audio)
			try:

				print("alexa thinks you said:" +text_t)
				app=text_t
				os.system('sudo apt remove '+app.lower())
			except:
				print("alexa could not understand audio")
				pass

	except Exception as e:
		print("alexa could not understand audio")
	pass
