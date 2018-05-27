#!/usr/bin/python3

#importing essential libs
#speech recognition lib based on gtts
import speech_recognition as sr
import os
#google text to speech
from gtts import gTTS
import subprocess
import time,webbrowser
from io import BytesIO

#to record the voice instruction
r=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
	#reduce the ambient noise
	r.adjust_for_ambient_noise(source)
	audio=r.listen(source)
response=""
text=""
x=1
result=""
try:
	#converting to text from online google speech to text api
	text=r.recognize_google(audio)
	text_t=text.lower()

	#the command said by user
	print(text_t)

	#performing the operation on ubuntu
	x = os.system(text_t)

	#checking if command run successfully(os.system returns 0)
	if(x==0):
		result = subprocess.check_output([text_t])
		
		#printing the output of the commands if run successfully
		print(result)
		tts = gTTS(result.decode(),lang='en')
		tts.save("hello.mp3")
		#ubuntu will reply wth the output
		os.system('mpg321 hello.mp3')
	#if commands was wrong then search it on google
	else:
		result = subprocess.check_output([text_t])
		tts = gTTS(result,lang='en')
		tts.save("hello.mp3")
		os.system('mpg321 hello.mp3')
		webbrowser.open_new_tab("http://www.google.com/search?q="+result)
#possible errors detected till now
except sr.RequestError:
	response+="API unavailable"
	tts = gTTS(response,lang='en')
	tts.save("hello.mp3")
	os.system('mpg321 hello.mp3')
	print(response)

except sr.UnknownValueError:
	response+="Unable to recognize speech"
	print(response)
	tts = gTTS(response,lang='en')
	tts.save("hello.mp3")
	os.system('mpg321 hello.mp3')
	print(response)

#if any error left
except Exception as e:
	print(e)





