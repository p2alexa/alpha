#!/usr/bin/env python3

import speech_recognition as sr
from gtts import gTTS
#import commands
import os
import subprocess
'''
r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Say something!")
  audio = r.listen(source)
  text_t= r.recognize_google(audio)
'''
def vcr(text):
	try:
		print("alexa thinks you said " +text_t)
		#print (commands.getstatusoutput('r.recognize_google(audio)'))
		#os.system("r.recognize_google(audio)")
		#subprocess.call(r.recognize_google(audio))
		result = subprocess.check_output([text_t])

		#printing the output of the commands if run successfully
		print(result)
		tts = gTTS(result.decode(),lang='en')
		tts.save("hello.mp3")
		#ubuntu will reply wth the output
		print(result)
		os.system('mpg321 hello.mp3')
	except:
		response="alexa could not understand audio"
		print(response)
		tts = gTTS(response,lang='en')
		tts.save("hello.mp3")
		os.system('mpg321 hello.mp3')
		pass

#os.system(r.recognize_google(audio))
