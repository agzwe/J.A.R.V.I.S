import pyttsx3  
import datetime  
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os  
import pyautogui
import psutil  
import pyjokes  
import requests, json  
import webbrowser
import time

wel = pyttsx3.init()
wel.setProperty('rate', 190)
voices = wel.getProperty('voices')
wel.setProperty('voice', voices[1].id)
wel.setProperty('volume', 1)

def speak(audio):
    wel.say(audio)
    wel.runAndWait()
def takecmd():
    cmd = sr.Recognizer()
    with sr.Microphone() as mic:
        print('say command......')
        cmd.phrase_threshold=1
        audio= cmd.listen(mic)
        try:
            print("recording.....")
            query = cmd.recognize_google(audio , language='en') 
            print(f"you said:{query}")
        except Exception as error:
            return None
        return query .lower()

        
def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "C:\\Users\\Jarvis-AI-using-python3-\\screenshots\\ss.png"
    )


speak('hello')
while True:
    query = takecmd()
    if 'hello' in query:
        speak ("faaaake you")

    elif 'open google' in query:
        speak ('ok')
       # time.sleep(3)
        webbrowser.open_new_tab('https://www.google.com')


    elif('i am done' in query or 'bye bye jarvis' in query
         or 'go offline jarvis' in query or 'bye' in query
          or 'nothing' in query):
             wishme_end()

    elif ("screenshot" in query):
        screenshot()
        speak("Done!")

    elif ("search on google" in query or "open website" in query):
         speak("What should i search or open?")
         chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
         search = takecmd().lower()
         wb.get(chromepath).open_new_tab(search + '.com') 