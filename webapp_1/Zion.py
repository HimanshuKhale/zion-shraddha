import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia    #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil   #pip install psutil
import pyjokes  #pip install pyjokes
import os   
import sys          
import pyautogui    #pip install pyautogui
import random
import json     
import requests
from urllib.request import urlopen
from newsapi import NewsApiClient   #pip install newsapi-python
import wolframalpha     #pip install wolframalpha
import time

engine = pyttsx3.init()
wolframalpha_app_id = 'HVH266-VGYAJ9W6YH'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M")
    speak("It's about")
    speak(Time)
    speak("by my clock")
time_()

def date_():
    Date=datetime.datetime.today().strftime('%Y-%m-%d')
    speak("Today is")
    speak(Date)
date_()

#Greet Me Fuction

def wishme():
    speak("AHOY!")
    date_()
    time_()
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir!, Welcome back!! what are we planning today")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir! Lets get cracking!")

    elif hour>=18 and hour<24:
        speak("Good Evening Sir. Still working, are we?")

    else:
        speak("Good Night, Sir")
    speak("What can I help you with?")

#wishme()

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio, language = "en-US")
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

#TakeCommand()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('zion.assistant.hk@gmail.com', 'Rabbitsfoot#1')
    server.sendmail('zion.assistant.hk@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)
    
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/HP/Pictures/screenshot/image.png")

if __name__ == "__main__":
    #wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace('wikipedia', " ")
            result = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(result)
            speak(result)
            
            speak('Okay, anything else?')
       
        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                
                speak("To whom should I send it to?")
                receiver = input("Enter the receiver's mail ID: ")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak("Email has been sent.")
                speak('anything else?')

            except Exception as e:
                print(e)
                speak("Unable to send the mail.")
            
                speak('Try again, anything else?')

        elif 'open in chrome' in query:
            speak('what should i search?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search, '.com')
            speak('Okay, anything else?')

        elif 'sugar' in query:
            speak('what is the destination?')
            dest_port = TakeCommand()

            speak('what will be per metric ton ocean freight? ')
            oft = input(" what is the ocean freight")

            speak("what is the base rate of sugar?")
            
            base = float(input("what is the base rate of sugar"))

            exf = base + base*0.0002        #0.1% TDS & 0.1% GST

            fob = exf + 3.1                 #Transport, CHA, brokerage

            fob_usd = ((fob*27000)/27)/74.5 

            pmt = float(fob_usd) + float(oft)


            speak("Today, the minimum rate for")
            speak(dest_port) 
            speak("would be") 
            speak( pmt)
            print("minimum rate for", dest_port, "is", pmt)
            speak('Okay, anything else?')



        elif 'search youtube' in query:
            speak("what should i search?")
            search_term = TakeCommand().lower()
            speak("opening youtube")
            wb.open('https://www.youtube.com/results?search_query=' +search_term)
            speak('Okay, anything else?')

        elif 'search google' in query:
            speak("What should I search?" )
            google_search = TakeCommand().lower()
            speak('All right, I am on it')
            wb.open('https://www.google.com/search?q=' + google_search)
            speak('Okay, anything else?')

        elif 'cpu' in query:
            cpu()

        elif 'dollar rate' in query:
            wb.open('https://finance.yahoo.com/quote/USDINR=x?ltr=1')
            speak('There you go, anything else?')

        elif 'joke' in query:
            joke()

        elif 'thanks' in query:
            speak('Going Offline!')
            quit()

        elif 'word' in query:
            speak("opening word application")
            word=r"C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.EXE"
            
            os.startfile(word)

        elif 'tax invoice details' in query:
            tax_file = r'E:\Downloaded Files\Download 2021\Tax Invoice (1).xlsx'
            os.open(tax_file, os.O_RDWR)


        elif 'excel' in query:
            speak("opening excel application")
            excel=r"C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE"
            
            os.startfile(excel)

        elif 'write a note' in query:
            speak('let me take out my pen and quill')
            notes = TakeCommand()
            file = open('notes.txt', 'w')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(':-')
            file.write(notes)

        elif 'show note' in query:
            speak('opening the notes')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'music' in query:
            songs_dir = 'G:/songs'
            music = os.listdir(songs_dir)
            speak('what should i play')
            ans = TakeCommand().lower()
            while('number' not in ans and ans!= 'surprise me'):
                speak("I didn't understand, please repeat")
                ans=TakeCommand()
            if 'number' in ans:
                no = int(ans.replace('number', ''))
            if 'surprise me' in ans:
                no = random.randint(1, 100)

            os.startfile(os.path.join(songs_dir, music[no]))

        elif 'note' in query:
            memory = TakeCommand()
            speak("When should I remind you of "+memory)
            remember =open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'recall the notes' in query:
            remember = open('memory.txt', 'r')
            speak('you said the following'+remember.read())

        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("Locating"+location)
            wb.open_new('https://www.google.com/maps/place/'+location)

        elif 'navigate' in query:
            speak('where should I take you to?')
            findme = TakeCommand().lower()
            speak("searching"+findme)
            wb.open_new_tab('https://www.google.com/maps/search/'+findme)

        elif 'news' in query:
            try:
                jsonObject = urlopen("https://newsapi.org/v2/business/language-en/country=id&apiKey=6d562cda226c48c2bee0c411a83ae5a7")
                data = json.load(jsonObject)
                i=1

                speak("Here are the top headlines from India")
                print("=======TOP HEADLINES=========")

                for item in data['articles']:
                    print(str(i)+ '. ' + item['title'] + '\n' )
                    print(item['description']+ '\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The asnwer is: "+answer)
            speak("The answer is :" + answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results Found")        

        elif "stop listening" in query:
            speak ('for how many seconds?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")