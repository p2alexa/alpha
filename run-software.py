#!/usr/bin/env python3

import speech_recognition as sr
import subprocess
import os
r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source)  # here
  print("Say something!")
  audio = r.listen(source)

try:

	print("google thinks you said:" +r.recognize_google(audio))
	x=r.recognize_google(audio)
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
	print("Google Speech Recognition could not understand audio")
	pass

