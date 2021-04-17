

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



def takeCommand():          # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=4000
        audio = r.listen(source)

    try:

        print("recognising...")
        quary=r.recognize_google(audio, language='en-in')   # here we using google for voice recognition
        #print(f"user said: {quary}")
    
    except Exception as e:
        print("say that again please")         # It ill be printed in case of improper voic
        return "none"
    return quary

if __name__=="__main__":                      # calling speak function inside my main function
    wishme()
    speak(" i am jabisu how can i help you ") # inside this speak function what u write is speaks by our AI
    
    while True:

     quary=takeCommand().lower()

     if 'wikipedia' in quary:                     # search on wikipedia 
         speak('searching wikipedia..')
         quary = quary.replace("wikipedia","")
         results = wikipedia.summary(quary, sentences=2)
         speak("according to wikipedia")
         print(results)
         speak(results)

     elif 'open youtube' in quary:        #opening youtube
         webbrowser.open("youtube.com")
        
     elif 'open google' in quary:           #opening google
         webbrowser.open("google.com")

     elif 'open stackoverflow' in quary:     #opening stackoverflow
         webbrowser.open("stackoverflow.com")

     elif 'play music' in quary:            # play music by follow the given path
         music_dir = 'C:\\Users\\User\\Downloads\\music'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[3])) 
    
     elif 'search on chrome' in quary:        # we can search on chrome by using this function
        speak(" what should i search sir ")
        search = takeCommand()
        chromepath = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
        webbrowser.get(chromepath).open_new_tab(search+'.com')

     elif 'open news' in quary:                  # check news only saying open news
        webbrowser.open('dainikbhaskar.com')    

     elif 'headache tablet' in quary:                     # we attache multiple tablets and our Ai tell us which tablet you take for that particular disease
        speak("you can take a aspirin tablet it will give you some relief ")

     elif 'fever' in quary:                         # like that
        speak("you can take a paracetamol tablet")
        
     elif 'current time' in quary:                     # shows present time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

     elif 'quit' in quary:
        quit()
     elif 'exit' in quary:         # exit by giving exit command
        break      
     else:
        speak("i can't listen")           
