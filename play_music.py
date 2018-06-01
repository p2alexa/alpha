#!/usr/bin/env python3

#pip3 install playsound
from gtts import gTTS
import playsound
import speech_recognition as sr
import os

import getpass
'''
r = sr.Recognizer()
with sr.Microphone() as source:
r.adjust_for_ambient_noise(source)  # here
print("Which song you want to play from your music folder?")
os.system("espeak 'Which song you want to play from your music folder?'")
audio = r.listen(source)
'''



def play_song(text):
	try:
		
		usr=getpass.getuser()
		print("alexa thinks you said:" +text)
		r = sr.Recognizer()

		with r as source:
			r.adjust_for_ambient_noise(source)  # here
			print("Which song you want to play from your music folder?")
			os.system("espeak 'Which song you want to play from your music folder?'")
			audio = r.listen(source)

		song=r.recognize_google(audio)

		try:
			playsound.playsound('/home/'+usr+'/Music/'+song, True)

		except:
			print("Sorry, you have to first download this song!")
			os.system("espeak 'Sorry, you have to first download this song!'")
	
	except Exception as e:
		print("alexa could not understand audio",e)
	pass
