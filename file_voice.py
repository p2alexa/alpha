#!/usr/bin/python3

#importing necessary libraries and modules
import pyttsx3
import speech_recognition as sr
import os
import time
from gtts import gTTS
import os.path
import shutil

#creating the object
r=sr.Recognizer()
mic=sr.Microphone(device_index=4)

global t
global audio

#function for taking input from user in audio and converting it into text
def getting_input():
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio=r.listen(source,timeout=10)
	print("DONE!!!")
	t=r.recognize_google(audio)
	print("converting audio into text")
	repeating_text(t)
	return t

#function for speaking as said by user
t1="hey"
def repeating_text(t1):
	tts=gTTS(text=t1, lang='en')
	tts.save("sps.wav")
	os.system("mpg321 sps.wav")

#
a='''
You can perform these operations:
1. Creating a new file(at home or current location).
2. Deleting the existing file.
3. Opening a file.
4. Copying a file into another file.
5. Listing the file names by size.
6. listing the file names by their types.
'''

list1=[]
#getting user input
def input_1():
	print(a)
	repeating_text("choose an operation")
	print("which one???")
	t=getting_input()
	list1=[]
	list1=t.split()
	print(list1)
	#return list1

	if('file' in list1 ):	
		if( list1[0] == 'create'):
				temp_list = ['create']

				#taking file name from user
				file_name=[]

				if(list1[-1]=='file'):
					file_name1=repeating_text("Please give name of file:")
					print("name of the file is  ")
					file_name1=getting_input()
					file_name.append(file_name1)
				else:
					file_name1=list1[-1]
					file_name.append(file_name1)	

				#taking location from user
				loc=repeating_text("please give the location :")
				print("current location or home directory")
				print("where  ")
				loc=getting_input()
				print(loc)
				repeating_text("the current directory location is:")
				repeating_text(os.getcwd())
				if(loc=='current'):
					repeating_text("Do you want to create a subdirectory  ")
					print("yes or no..   ")
					req=getting_input()
					#str_1="no"
					#str_2="yes"
					if(req == 'no'):
						#if user wants to create a file at this location only
						here = os.path.dirname(os.path.realpath(__file__))
						#joining the filename with its  current path
						filepath = os.path.join(here, file_name[0])
						repeating_text("Successfully created a file ")
						time.sleep(1)
						repeating_text("Check it out!!!")

						# create an empty file.
						try:
							f = open(filepath, 'w')
							f.close()
						except IOError:
							repeating_text("Wrong path provided")
							print("Please try again")


					else:	
						repeating_text("Please give the name of subdirectory  ")
						print("name is :  ")
						sub_dir_name=getting_input()
						here = os.path.dirname(os.path.realpath(__file__))
						filepath = os.path.join(here, sub_dir_name, file_name[0])
						repeating_text("Successfully created a file inside the directory")
						time.sleep(1)
						repeating_text("lo hogya aapka kaam")
						print("Check it out!!!")

						#creating your subdirectory
						os.mkdir(os.path.join(here, sub_dir_name))

						#create an empty file.
						try:
							f = open(filepath, 'w')
							f.close()
						except IOError:
							repeating_text("Wrong path provided")
							print("Please try again")	

#for deleting the file
	if('file' in list1):
			if('delete' in list1[0] || 'remove' in list1[0]):
						temp_list=['delete']
						file_name=[]
						if(list1[-1]=='file'):
							#getting file name to delete
							repeating_text("Please give name of file:")
							print("name is : ")
							file_name1=getting_input()
							file_name.append(file_name1)

						else:
							file_name1=list1[-1]
							file_name.append(file_name1)
						loc=repeating_text("please give the location :")
						print("current location or home directory")
						print("where :  ")
						loc=getting_input()
						print(loc)
						repeating_text("the current directory location is:")
						repeating_text(os.getcwd())
								
						if(loc=='current'):
								repeating_text("Do you want to delete a subdirectory  ")
								print("yes or no  ")
								req=getting_input()
								#str_1="no"
								#str_2="yes"
								if(req == 'no'):
									#if user wants to delete a file from this location only
										if(os.path.isfile(file_name)):
												os.remove(file_name)
												repeating_text("Successfully deleted a file ")
												time.sleep(1)
												repeating_text("ab toh krdi delete..ab kya dekhna!!!!")
										else:
												repeating_text("Please give a valid file name")
												print("File not exist",file_name)    		
								else:
									repeating_text("Please give the name of subdirectory  ")
									print("name is  ")
									sub_dir_name=getting_input()
									if(os.path.isDirectory(sub_dir_name)):
										shutil.remove(sub_dir_name)
									else:
										repeating_text("please give a valid file name")
										print("Directory not exist",sub_dir_name)

	if('file' in list1):
			if(list1[0] == 'open'):
						temp_list=['delete']
						file_name=[]
						if(list1[-1]=='file'):
							repeating_text("Please give name of file:")
							print("name is : ")
							file_name1=getting_input()
							file_name.append(file_name1)

						else:
							file_name1=list1[-1]
							file_name.append(file_name1)
						loc=repeating_text("please give the location :")
						print("current location or home directory")
						print("where :  ")
						loc=getting_input()
						print(loc)
						if(loc=='current'):
							open_file=open(file_name,'w')
							repeating_text("the file is being opened")
						else:
							open(file_name,'w')
						
	if('file' in list1):
			if(list1[0] == 'copy'):


									   	
input_1()  
	