#!/usr/bin/env python3

import speech_recognition as sr
from gtts import gTTS
import subprocess
import os
from gtts import gTTS
'''
r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Say something!")
  audio = r.listen(source)
'''
def run_sw(text):
	try:

		print("alexa thinks you said:" +text)
		tts = gTTS(text,lang='en')
		tts.save("hello.mp3")
		os.system('mpg321 hello.mp3')
		x=text
		if 'VLC' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "vlc")])
		if 'soul' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "games", "sol")])
		if 'mahajon' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "games", "gnome-mahjongg")])
		if 'mind' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "games", "gnome-mines")])
		if 'Sudoku' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "games", "gnome-sudoku")])
		if 'bitmap' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "bitmap")])
		if 'Bluetooth' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "bluetooth-wizard")])
		if 'map' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "charmap")])
		if 'cheese' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "cheese")])
		if 'image' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "eog")])#imageviewer
		if 'edit' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "gedit")])
		if 'calculator' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "gnome-calculator")])
		if 'calendar' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "gnome-calendar")])
		if 'screenshot' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "gnome-screenshot")])
		if 'terminal' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "gnome-terminal.real")])
		if 'clock' in x:
			p = subprocess.Popen([os.path.join("/", "usr", "bin", "xclock")])
	except:
		response="alexa could not understand audio"
		print(response)
		tts = gTTS(response,lang='en')
		tts.save("hello.mp3")
		os.system('mpg321 hello.mp3')
		pass

