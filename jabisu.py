

import pyttsx3                                # A python library that will help us to convert text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')                # Microsoft developed speech API Helps in synthesis and recognition of voice.
voices = engine.getProperty('voices')
# print('voices',voices[0].id)                # it is not necessary to print languages so i comment out this function 
engine.setProperty('voice',voices[0].id)      # setting the voices 



def speak(audio):                             # we will write our speak() function to convert our text to speech
    engine.say(audio)     
    engine.runAndWait()                       # without these function we can't hear the audio 


def wishme():                                 # declaring wishme function
    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak(" good morning")
    elif hour>=12 and hour<18:
        speak(" good afternoon")
    else:
        speak(" good evening")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=4000
        audio = r.listen(source)

    try:

        print("recognising...")
        quary=r.recognize_google(audio, language='en-in')
        print(f"user said: {quary}\n")
    
    except Exception as e:
        print("say that again please")
        return "none"
    return quary

if __name__=="__main__":                      # calling speak function inside my main function
    wishme()
    speak(" i am jabisu how can i help you ") # inside this speak function what u write is speaks by our AI
    
    while True:

     quary=takeCommand().lower()

     if 'wikipedia' in quary:
         speak('searching wikipedia..')
         quary = quary.replace("wikipedia","")
         results = wikipedia.summary(quary, sentences=2)
         speak("according to wikipedia")
         print(results)
         speak(results)

     elif 'open youtube' in quary:
         webbrowser.open("youtube.com")
        
     elif 'open google' in quary:
         webbrowser.open("google.com")

     elif 'open stackoverflow' in quary:
         webbrowser.open("stackoverflow.com")

     elif 'play music' in quary:
         music_dir = 'C:\\Users\\User\\Downloads\\music'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[3])) 

     elif 'quit' in quary:
        quit()
     elif 'exit' in quary:
        break      
     else:
        speak("i can't listen")           
