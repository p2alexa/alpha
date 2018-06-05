#!/usr/bin/env python3

#Test by trying vlc

import speech_recognition as sr
import os

r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Do you want to install or remove an application or command?")
  os.system("espeak 'Do you want to install or remove an application or command?'")
  audio = r.listen(source)

try:
	
	print("google thinks you said:" +r.recognize_google(audio)) #test with vlc
	xyz=r.recognize_google(audio)

	if 'install' in xyz:
		print("Which application or command do you want to install?")
		os.system("espeak 'Which application or command do you want to install?'")
		r = sr.Recognizer()

		with sr.Microphone() as source:
  			r.adjust_for_ambient_noise(source)  # here
  			audio = r.listen(source)
  
		try:

			print("google thinks you said:" +r.recognize_google(audio))
			app=r.recognize_google(audio)
			os.system('sudo apt install '+app.lower())
		except:
			print("Google Speech Recognition could not understand audio")
			pass
	
	if 'remove' in xyz:
		print("Which application or command do you want to remove?")
		os.system("espeak 'Which application or command do you want to remove?'")
		r = sr.Recognizer()

		with sr.Microphone() as source:
  			r.adjust_for_ambient_noise(source)  # here
  			audio = r.listen(source)
  
		try:

			print("google thinks you said:" +r.recognize_google(audio))
			app=r.recognize_google(audio)
			os.system('sudo apt remove '+app.lower())
		except:
			print("Google Speech Recognition could not understand audio")
			pass

except:
	print("Google Speech Recognition could not understand audio")
	pass
