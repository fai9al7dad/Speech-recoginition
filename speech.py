import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()

def recordvoice(ask = False):
    with sr.Microphone() as source:
        audio = r.listen(source)
        if ask:
            speak(ask)
        voicedata=''
        try:
            voicedata = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand you")
        except sr.RequestError:
            speak('Sorry, My services are down')
    return voicedata

def speak(audio_string):
    tts= gTTS(text=audio_string, lang='en')
    r =random.randint(1,100000000)
    audiofile = 'audio-'+str(r)+'.mp3'
    tts.save(audiofile)
    playsound.playsound(audiofile)
    print(audio_string)
    os.remove(audiofile)

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak("Faisal haddad")
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search = recordvoice("What do you want to search for?")
        url = "www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak('here is what i found for ' + search)
    if 'find location' in voice_data:
        location = recordvoice("What do you want to find?")
        url = "www.google.com/maps/place/'" + location + "'/&amp;"
        webbrowser.get().open(url)
        speak('here is the location for ' + location)
    if 'how old are you' in voice_data:
        speak("20")
    if 'who is the best teacher' in voice_data:
        speak("Khalid aslani")
    if 'exit' in voice_data:
        exit()

speak("How can i help you?")
voicedata = recordvoice()
respond(voicedata)
