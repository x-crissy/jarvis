import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio


MASTER = "Rishabh"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
     engine.say(text)
     engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning bro" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon bro" + MASTER)

    else:
        speak("good evening bro" + MASTER)

    speak("I am code GREY. How may i help you?")        


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please") 
        query = None

    return query    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('deadlinekiller50@gmail.com', 'unknownpwd')
    server.sendmail("rishavsinghraj1@gmail.com")
    server.close()
speak("initializing Jarvis....")
wishMe()
query = takeCommand()
if 'wikipedia' in query.lower():
    speak('Searchiing wikipedia...')
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences =2)
    print(result)
    speak(result)
    
elif 'open youtube' in query.lower():
    # webbrowser.open("youtube.com")
    speak('have fun')
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
   # url = ""
if 'more' in query.lower():
    #speak('i am jarvis created by rishabh sir. Date- 12/02/21 , project number 5')
    result = 'i am jarvis created by rishabh sir. Date- 02/12/21 , project number 5'
    print(result)
    speak(result)

elif 'hangout' in query.lower():
    speak('chat!! goes on')
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://hangouts.google.com/u/3/?authuser=3")

elif 'google' in query.lower():
    speak('knowlwdge')
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")

#elif 'play music' in query.lower():
    #songs = os.listdir("C:/Users/Public/Music/Sample Music")
    #print(songs)

elif 'the time' in query.lower():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strtime}")

elif 'open code' in query.lower():
    codePath = "E:\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'email to Rishabh' in query.lower():
    try:
        speak("What should i send")
        content = takeCommand()
        to = "rishavsinghraj1@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent")

    except Exception as e:
        print(e)  

elif 'open powerpoint' in query.lower():
    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk"
    os.startfile(codePath)

elif 'open zoom' in query.lower():
    codePath = "C:\\Users\\new\\Desktop\\Zoom.lnk"
    os.startfile(codePath)

elif 'play music' in query.lower():
    codePath = "C:\\Users\\new\\Desktop\\Spotify.lnk"
    os.startfile(codePath)
engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please") 
        query = None

    return query
    
query = takeCommand()
if 'wikipedia' in query.lower():
    speak('Searchiing wikipedia...')
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences =2)
    print(result)
    speak(result)
    
elif 'open youtube' in query.lower():
    # webbrowser.open("youtube.com")
    speak('have fun')
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
   # url = ""
if 'more' in query.lower():
    #speak('i am jarvis created by rishabh sir. Date- 12/02/21 , project number 5')
    result = 'i am jarvis created by rishabh sir. Date- 02/12/21 , project number 5'
    print(result)
    speak(result)

elif 'hangout' in query.lower():
    speak('chat!! goes on')
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://hangouts.google.com/u/3/?authuser=3")

elif 'google' in query.lower():
    speak('knowlwdge')
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")

#elif 'play music' in query.lower():
    #songs = os.listdir("C:/Users/Public/Music/Sample Music")
    #print(songs)

elif 'the time' in query.lower():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strtime}")

elif 'open code' in query.lower():
    codePath = "E:\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'email to Rishabh' in query.lower():
    try:
        speak("What should i send")
        content = takeCommand()
        to = "rishavsinghraj1@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent")

    except Exception as e:
        print(e)  

elif 'open powerpoint' in query.lower():
    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk"
    os.startfile(codePath)

elif 'open zoom' in query.lower():
    codePath = "C:\\Users\\new\\Desktop\\Zoom.lnk"
    os.startfile(codePath)

elif 'play music' in query.lower():
    codePath = "C:\\Users\\new\\Desktop\\Spotify.lnk"
    os.startfile(codePath)
	