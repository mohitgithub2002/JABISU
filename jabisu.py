# WITH THIS WHOLE CODE OUR JABISU IS READY TO SPEAK

import pyttsx3                                # A python library that will help us to convert text to speech


engine = pyttsx3.init('sapi5')                # Microsoft developed speech API Helps in synthesis and recognition of voice.
voices = engine.getProperty('voices')
# print('voices',voices[0].id)                # it is not necessary to print languages so i comment out this function 
engine.setProperty('voice',voices[0].id)      # setting the voices 



def speak(audio):                             # we will write our speak() function to convert our text to speech
    engine.say(audio)     
    engine.runAndWait()                       # without these function we can't hear the audio 

if __name__=="__main__":                      # calling speak function inside my main function

    speak(" i am jabisu how can i help you ") # inside this speak function what u write is speaks by our AI
  