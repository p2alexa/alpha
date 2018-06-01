#!/usr/bin/python3
import speech_recognition as sr
import urllib
import urllib.parse
import webbrowser
import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import os
from gtts import gTTS 
import google_youtube, run_software, voice_cmd_run, install_sw, play_music


#listening to user
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)  # here
	print("WHat operation do you want to perform ?")
	os.system("espeak 'What operation do you want to perform ?'")
	audio = r.listen(source)
text=r.recognize_google(audio)

#for searching on internet
if 'google' in text or 'youtube' in text:
	print("google or youtube")
	google_youtube.ggl_yt(text)

#for running desktop application
elif ('application' in text or 'app' in text):
	print("application")
	run_software.run_sw(text)

#for running terminal commands
elif 'command' in text:
	print("command")
	list1=text.split()
	index1=list1.index('command')+1
	voice_cmd_run.vcr(str(list1[index1]))

#for installing application
elif 'install' in text or 'remove' in text:
	print('installation')
	install_sw.install_pkg(text)

#for playing songs from computer or from youtube
elif 'play' in text or 'music' in text:
	print('music')
	play_music.play_song(text)
