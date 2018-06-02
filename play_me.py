#!/usr/bin/python3
from gtts import gTTS
import os
import speech_recognition
from nltk.tokenize import word_tokenize
#import listener
import subprocess
import getpass
def play_song(text):
	print('alexa thinks you said',text)
	print('which song would you like to play')
	try:
		#text=listener.listen()
		text=str(input('enter song name'))
		print('alexa thinks you said',text)
		text="\ ".join(text.split())
		#text_splitted=word_tokenize(text)
		#kind of messy thing done here
		#just let you know it searches for the song among all the songs in music dir
		#if all(x in subprocess.check_output('ls /home/'+getpass.usrname()+'Music/').decode().split('\n') for x in text):
		try:
			result = subprocess.check_output('find /home/'+getpass.getuser()+'/Music/ -iname *'+text+'*',shell=True).decode()
			if result == "":
				print("could not find the song")
			else:
				print(result.split("\n"))
				song_list=result.split('\n')
				#there may be multiple songs containing keywords user said but we choose the song which is first
				song="\ ".join(song_list[0].split())
				print(song)
				os.system('vlc '+song)
			
		except Exception as e:
			print("oops... looks like I could not find the song you asked.",e)
	except:
		print("alexa could not understand what you said")

play_song("play a song")
		
		
	
	
