from email.mime import audio
from mimetypes import init
from types import TracebackType
from urllib.request import ProxyBasicAuthHandler
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
from googlesearch import search
import json
import requests
import random
import speedtest
import os
from keyboard import press
from keyboard import press_and_release
import pywhatkit
import speech_recognition as sr

#defining the engine 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# narrates the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()
    return 

# greets accordingly with the time
def greetings():
    hour = datetime.datetime.now().hour
    if (hour < 12):
        speak('Good Morning sir')
    elif (hour < 18):
        speak('Good afternoon sir')
    else :
        speak('Good evening sir')    

    speak('i am Windows Assistant. What can i do for you')

#takes input from the microphone 
def takeCommand():
    rec = sr.Recognizer() 
    with sr.Microphone() as source:
        print("What can i do for you...")
        audio = rec.listen(source)
        rec.pause_threshold = 1

    try:
        print('Recognizing...')
        query = rec.recognize_google(audio, language = 'en-in')
        print(f'you said: {query}\n')
        # return "a" if len(query) == 0 else query
        return query.lower()

    except Exception as e:
        # speak('Could you please repeat th at')
        return "a"

#take notes in notepad
def Notepad():
    speak("Tell me the Query.")
    speak("I am Ready to write.")
    note = takeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = time.replace(":", "-") + "-note.txt"

    with open(filename, "w") as file:
        file.write(note)

    path_1 = "E:\\python\\Desktop assistant\\" + str(filename)
    path_2 = "E:\\python\\Desktop assistant\\Notes\\" + str(filename)

    os.rename(path_1, path_2)
    os.startfile(path_2)

def Close_Notepad():
    os.system("TASKKILL /F /IM Notepad.exe")
    return

#open system apps
def OpenApps():
    speak("wait a second sir!")

    if 'code' in audioInput:
        os.startfile("C:\\Users\\UserName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'discord' in audioInput:
        os.startfile("C:\\Users\\UserName\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")

    elif 'edge' in audioInput:
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    
#main 
if __name__ == "__main__":

    print("Initializing...")
    speak("Initializing...")

    greetings()

    while True:
        audioInput = takeCommand().lower()

        if ('open google' == audioInput):
            speak('Opening Google...')
            url = "https://www.google.com/"
            webbrowser.open(url)

        elif(audioInput.endswith('in chrome')):
            if ('new tab' in audioInput):
                press_and_release('ctrl + t')

            elif ('close tab' in audioInput):
                press_and_release('ctrl + w')

            elif ('new window' in audioInput):
                press_and_release('ctrl + n')

            elif ('refresh tab' in audioInput):
                press_and_release('ctrl + r')

            elif ('switch tab' in audioInput):
                press_and_release('ctrl + tab')

            elif ('downloads' in audioInput):
                press_and_release('ctrl + j')

            elif ('history' in audioInput):
                press_and_release('ctrl + h')

            else :
                continue

        elif ('open youtube' == audioInput):
            speak('Opening YouTube...')
            url = "https://www.youtube.com/"
            webbrowser.open(url)

        elif ('change window' in audioInput):
            press_and_release('alt + tab')

        elif ('take screenshot' in audioInput):
            press_and_release('ctrl + shift + s')

        elif ('time' in audioInput):
            time = datetime.datetime.now().strftime("%H:%M")    
            print("time : " + time)
            speak(time)

        elif ('google' in audioInput) :
            speak('Searching for...')
            audioInput = audioInput.replace("Google", "")
            speak(audioInput)
            url = "https://www.google.com/search?q={}".format(audioInput)
            webbrowser.open(url)


        elif ('news' in audioInput):
            speak('Fetching news articles...')
            response = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=c2cd6ea35abc474e8e6b071519621ada')
            json_data = json.loads(response.content)
            n = random.randint(1, 15)
            title = json_data['articles'][n]['title']
            link = json_data['articles'][n]['url']
            webbrowser.open(link)
            speak(title)

        elif ('playlist' in audioInput):
            speak('Playing music...')
            webbrowser.open('https://music.youtube.com/watch?v=LZ-Qn4q3sbU&list=RDCLAK5uy_n9Fbdw7e6ap-98_A-8JYBmPv64v-Uaq1g')

        elif ('internet speed' in audioInput):
            speak('Checking internet speed...')
            speak("Please wait....")
            speed = speedtest.Speedtest()    
            downloadSpeed = speed.download()
            ds = int(downloadSpeed/800000)
            uploadSpeed = speed.upload()
            us = int(uploadSpeed/800000)
            print(f"the downloading speed is {ds} mbps & uploading speed is {us} mbps")
            speak(f"the downloading speed is {ds} mbps & uploading speed is {us} mbps")

        elif 'take a note' == audioInput:
            Notepad()
            
        elif 'close notepad' in audioInput:
            Close_Notepad()

        elif 'open edge' in audioInput:
            OpenApps()

        elif 'open discord' in audioInput:
            OpenApps()

        else :
            continue

    
