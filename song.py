#!/usr/bin/env python3

#pip3 install playsound

import playsound
import speech_recognition as sr
import os
import os.path

r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Which song you want to play from your music folder?")
  os.system("espeak 'Which song you want to play from your music folder?'")
  audio = r.listen(source)

try:

	print("Google thinks you said:" +r.recognize_google(audio))
	song=r.recognize_google(audio)
	try:
		playsound.playsound('/home/rishabh/Music/'+song, True)
	except:
		print("Sorry, you have to first download this song!")
		os.system("espeak 'Sorry, you have to first download this song!'")
	
except:
	print("Google Speech Recognition could not understand audio")
	pass


