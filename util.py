#!usr/bin/pytho3

#importing essential libs
import speech_recognition as sr
import os,time,webbrowser
#from espeak import espeak
import subprocess
from gtts import gTTS
#import pyttsx
from io import BytesIO
import shutil

x='''

hello there! welcome to MUI ...
you can perform multiple tasks:

1.Say "make a directory" to make a new directory at current location or any location specified.

2.Say "Remove directory" to delete a directory.

3. Say "List directories" to list the directories at a loction by:
       1.all directories.
       2.by size.
       3.by type.

4.Say "open directory" Open a directory.

5.Say "Close directory" to Close a directory or say "close all directories" to close all the open directories.

6.Say "Empty a directory" to delete all its contents.

7.Say "Duplicate directory" to create a copy of directory with its contents.
'''
#funcion for speech recognition
def listen():
	r=sr.Recognizer()
	mic=sr.Microphone()
	with mic as source:
		#reduce the ambient noise
		r.adjust_for_ambient_noise(source)
		print("speak...")
		audio=r.listen(source,timeout=10)
	print("recognizing voice...")
	text=r.recognize_google(audio)
	text_t=text.lower()
	print("voice recognized...")
	return (text_t)

#function for text-to-speech
'''a="lol"
'''
def speak(a):
	tts = gTTS(text=a, lang='en')
	tts.save("good.mp3")
	os.system("mpg321 good.mp3")
	

#function for cleaning path list 
def clean_path(path):
	paths=path.split()                    #conditions to clean "in" and " " etc can be added
	return paths


#main function
#note:
#speech was not working in nested program so this program contains all the function via text although i have included all the speak() and listen() functions,


def main():
    print(x)
    speak("what do you want to do")
    text_t=listen()
    print (text_t)
    #text_t=str(input("what: ")).lower()

    #to make new directory
    if "make" in text_t and "directory" in text_t:
    	speak("where do you want to create a directory")
    	print ("current directory or other directory")
    	#loc=str(input("where: "))  
    	loc=listen()
    	print (loc)    	
    	if loc == "current directory":
    		speak("what is the directory name")
    		name=listen()
    		#name=str(input("name: "))
    		#making directory at current location
    		x=os.system('mkdir '+name.lower())		
		if(x==1):
			print("directory sucessfully created")
    	elif loc=="other directory":
    		path=listen()
    		#path=str(input("where: ")).lower()
    		path_f=clean_path(path)
    		y=""
    		for a in path_f:
    			y=y+str(a)+"/"
    		print(y)
    		#speak("what is the directory name")
    		#name=listen()
    		name=str(input("name: ")).lower()
    		os.system('mkdir '+y+name)

    #to remove a directory
    if text_t == "remove directory":
    	#speak("which directory")
    	#direc=listen()
    	direc=str(input("which: "))
    	temp=str('rm -r '+direc)
    	#speak("are you sure")
    	#ans=listen()
    	os.system(temp)
    	#speak("done")  	result = subprocess.check_output(temp)

    #listing directories
    if "list" in text_t and "directories" in text_t:
    	#list by type
    	if "hidden" in text_t:
    		listtemp="ls -a "
    		os.system(listtemp)
    		result = subprocess.check_output([listtemp])
    		print (result) #speak(result)
    	#list by size
    	elif "by" in text_t and "size" in text_t:
    		listtemp="ls -lhSgo | grep -v '^d' "
    		os.system(listtemp)
    		result = subprocess.check_output([listtemp])
    		print(result) #speak(result)
    	#listing all directories
    	else:
    		listtemp="tree -d"
    		os.system(listtemp)
    		result = subprocess.check_output([listtemp])
    		print(result)  #speak(result)

    #open a directory
    if "open" in text_t and "directory" in text_t:
    	#speak("which directory")
    	#path=listen()
    	path=str(input("which: ")).lower()
    	path_f=clean_path(path)
    	y=""
    	for a in path_f:
    		y=y+str(a)+"/"
    		print(y)
    		os.system('nautilus '+y)

    #close a directory
    if "close" in text_t and "directory" in text_t:
    	if "all" in text_t:
    		os.system('killall nautilus')
    	#os.system('nautilus -q')

    #empty a directory
    if "empty" in text_t and "directory" in text_t:
        #speak("which directory")
        #path=listen()
        path=str(input("which: ")).lower()
        if len(path) is 1:
        	y=path
        else:
        	path_f=clean_path(path)
        	y=""
        	for a in path_f:
        		y=y+str(a)+"/"
        		print(y)
        shutil.rmtree(y)

    #copy directory
    if "duplicate" in text_t and "directory" in text_t:
    	#path=listen()
    	#speak("which directory")
        path=str(input("which: ")).lower()
        if (len(path)==1):
            y=path

        else:
            path_f=clean_path(path)
            y=""
            for a in path_f:
                y=y+str(a)+"/"
                print(y)
        z=""
        z=y[-1]+"1"
        print(z)
        shutil.copytree(y,z)
main()



