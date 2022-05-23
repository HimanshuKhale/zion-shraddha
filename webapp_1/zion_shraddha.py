from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from num2words import num2words
import datetime
from datetime import date, timedelta
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
PATH = "F:\Drivers\chromedriver.exe"


name_dict={'alliance' : 'ALLIANCE DIVINE IMPEX PTE LTD', 
            'hiangli' : 'HIANG LI TRADING PTE LTD', 
            'anush lini' : 'ANUSH LINI LLC',
            'satrah general' : 'SATRAH GENERAL TRADING LLC', 
            'bharti general' : 'BHARTI OVERSEAS GENERAL TRADING LLC', 
            'p s yew' : 'P.S. YEW BROTHERS TRADING SDN BDH', 
            'BSRAT' : 'BSRAT DMCC DJIBOUTI BRANCH', 
            'chong sheng' : 'CHONG SHENG PTE LTD',
            'ensen' : 'ENSEN TRADING & INDUSTRY PVT LTD', 
            'farmex' : 'FARMEX FRESHIA TRADING LLC', 
            'global' : 'GLOBAL RISE TRADING PTE LTD',
            'mohiddin' : 'MOHIDDIN LANKA FOODSTUFF TRADING LLC', 
            'raj star' : 'RAJ STAR GENERAL TRADING LLC', 
            'a b c' : 'A B C IMPORTS & EXPORTS', 
            'galaxi' : 'GALAXI INTERNATIONAL FZCO', 
            'popular' : 'POPULAR MIDDLE EAST FZC',
            'far lee': 'FAR LEE PTE LTD', 
            'smart dragon' : 'SMART DRAGON LANKA PVT LTD',
            'devi global' : 'DEVI GLOBAL HK LTD'}

address_dict={
            'alliance' : 'No 160 Kallang Way #01-02 Singapore 349246', 
            'hiangli' : 'PO BOX 540, SINGAPORE POST CENTRE SINGAPORE 914028', 
            'anush lini' : 'MASIS STREET 50, YEREVAN, ARMENIA POST CODE: 0061',
            'satrah general' : 'AL ZAROONI BUILDING, 2ND FLOOR, FLAT NO. 3, AL RAS STREET, P.O. BOX: 26458, 64929, DEIRA, DUBAI- UAE', 
            'bharti general' : '2018 PARK LANE TOWER, BUSINESS BAY, DUBAI- UAE ', 
            'p s yew' : 'LOT 1, JALAN UTARID U5/16, MAH SING IND. PARK, SEKSYEN U5, 40150 SHAH ALAM, SELANGOR DARUL EHSAN', 
            'BSRAT' : 'DJIBOUTI INTERNATIONAL TOWER, DESK F-5V088 DIFTZ REPUBLIQUE DE DJIBOUTI', 
            'chong sheng' : '1 IRVING PLACE #08-01 THE COMMERZE@IRVING',
            'ensen' : 'F-107, PEOPLES PARK SHOPPING COMPLEX, COLOMBO 11, SRILANKA', 
            'farmex' : 'PO BOX 378993, AL RAS DEIRA-DUBAI, UAE', 
            'global' : '21, WOODLANDS CLOSE PRIME BIZ HUB, #08-44 SINGAPORE',
            'mohiddin' : 'SHOP NO. S1 PORT SAEED, PO BOX 118z838, AL RAS DEIRA-DUBAI, UAE', 
            'raj star' : 'RAJ STAR GENERAL TRADING LLC', 
            'a b c' : '25/2/1, 8TH LANE, COLOMBO 03, SRILANKA', 
            'galaxi' : 'AL GAMIL BUILDING, NIF CODE: 2031338, DJIBOUTI, REPUBLIC OF DJIBOUTI', 
            'popular' : 'PO BOX 932 AJMAN UNITED ARAB EMIRATES',
            'far lee': '39, WOODLANDS CLOSE, #07-05 MEGA@WOODLANDS SINGAPORE 73785', 
            'smart dragon' : 'NO.39A, COL.T.G.JAYAWARDANA MAWATHA, COLOMBO 03, SRI LANKA',
            'devi global' : 'ROOM 715A, 7/F, BLOCK A, VERISTRONG INDUSTRIAL CENTRE, 34-36, AU PUI WAN STREET,FO TAN HONGKONG'}

country_dict={
            'alliance' : 'SINGAPORE', 
            'hiangli' : 'SINGAPORE', 
            'anush lini' : 'ARMENIA',
            'satrah general' : 'UAE', 
            'bharti general' : 'UAE', 
            'p s yew' : 'MALAYSIA', 
            'BSRAT' : 'DJIBOUTI', 
            'chong sheng' : 'SINGAPORE',
            'ensen' : 'SRILANKA', 
            'farmex' : 'UAE', 
            'global' : 'SINGAPORE',
            'mohiddin' : 'UAE', 
            'raj star' : 'UAE', 
            'a b c' : 'SRILANKA', 
            'galaxi' : 'DJIBOUTI', 
            'popular' : 'UAE',
            'far lee': 'SINGAPORE', 
            'smart dragon' : 'SRILANKA',
            'devi global' : 'HONG-KONG'}

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
        r.pause_threshold = 0.5
        audio = r.listen(source, timeout=10)

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

        elif 'disposal' in query:
            party = input("who is the remitter? ")
            buyer = name_dict.get(party)
            address = address_dict.get(party)
            amount = input("what is the amount remitted?")
            amount_words = num2words(amount, to = 'currency')
            today = date.today()
            date=datetime.datetime.today().strftime('%d%m%Y')
            shipment_date = (today+timedelta(days=18)).strftime('%d-%m-%Y')
            last_shipment_date = (today+timedelta(days=94)).strftime('%d%m%Y')
            date_of_contract = (today+timedelta(days= -4)).strftime('%d%m%Y')
            proforma_invoice_no = input("what is the proforma invoice no. ? ")
            date_of_proforma = (today+timedelta(days= -8)).strftime('%d-%m-%Y')
            containers=float(input("what are the no. of containers? : "))
            bags = (containers * 540)
            bags_wt = float(0.00016)* float(bags)
            gross_wt = int((containers)*(27)) + bags_wt
            net_wt = int((containers*27))
            rate = int(float(total_amount)/float(net_wt))

            notify = input("is there any notify party?  y/n: ")

            if notify==y:
                notify_party = input("name the notify party")

            driver = webdriver.Chrome(PATH)

            new_url = "http://shraddhaimpex.epizy.com/720-2/"

            driver.get("http://shraddhaimpex.epizy.com/720-2/")

            driver.find_element_by_xpath("//*[@id='main']/div[2]/a[1]").click()

            driver.find_element_by_xpath('//*[id="amount"]').send_keys(amount)
            driver.find_element_by_xpath('//*[id="amount_words"]').send_keys(amount_words)
            driver.find_element_by_xpath('//*[id="buyer_address"]').send_keys(address)
            driver.find_element_by_xpath('//*[id="buyer_name"]').send_keys(buyer)
            driver.find_element_by_xpath('//*[id="d1"]').send_keys(d1)
            driver.find_element_by_xpath('//*[id="d2"]').send_keys(d2)
            driver.find_element_by_xpath('//*[id="m1"]').send_keys(m1)
            driver.find_element_by_xpath('//*[id="m2"]').send_keys(m2)
            driver.find_element_by_xpath('//*[id="y1"]').send_keys(y1)
            driver.find_element_by_xpath('//*[id="y2"]').send_keys(y2)
            driver.find_element_by_xpath('//*[id="y3"]').send_keys(y3)
            driver.find_element_by_xpath('//*[id="y4"]').send_keys(y4)
            driver.find_element_by_xpath('//*[id="1d1"]').send_keys(d1-1)
            driver.find_element_by_xpath('//*[id="1d2"]').send_keys(d2-1)
            driver.find_element_by_xpath('//*[id="1m1"]').send_keys(m1-1)
            driver.find_element_by_xpath('//*[id="1m2"]').send_keys(m2-1)
            driver.find_element_by_xpath('//*[id="1y1"]').send_keys(y1-1)
            driver.find_element_by_xpath('//*[id="1y2"]').send_keys(y2-1)
            driver.find_element_by_xpath('//*[id="1y3"]').send_keys(y3-1)
            driver.find_element_by_xpath('//*[id="1y4"]').send_keys(y4-1)
            driver.find_element_by_xpath('//*[id="2d1"]').send_keys(d1-2)
            driver.find_element_by_xpath('//*[id="2d2"]').send_keys(d2-2)
            driver.find_element_by_xpath('//*[id="2m1"]').send_keys(m1-2)
            driver.find_element_by_xpath('//*[id="2m2"]').send_keys(m2-2)
            driver.find_element_by_xpath('//*[id="2y1"]').send_keys(y1-2)
            driver.find_element_by_xpath('//*[id="1y2"]').send_keys(y2-2)
            driver.find_element_by_xpath('//*[id="2y3"]').send_keys(y3-2)
            driver.find_element_by_xpath('//*[id="2y4"]').send_keys(y4-2)

            driver.switch_to.window(driver.window_handles[1])
            driver.get(new_url)

            driver.find_element_by_xpath("//*[@id='main']/div[5]/a[1]").click()

            driver.find_element_by_xpath("//*[@id='Proforma-Invoice-No']").send_keys(proforma_invoice_no)
            driver.find_element_by_xpath("//*[@id='date']").send_keys(date_of_proforma)
            driver.find_element_by_xpath("//*[@id='buyer']").send_keys(buyer)
            driver.find_element_by_xpath("//*[@id='address']").send_keys(address)
            driver.find_element_by_xpath("//*[@id='notify party']").send_keys(notify_party)
            driver.find_element_by_xpath("//*[@id='notify party address']").send_keys(notify_address)
            driver.find_element_by_xpath("//*[@id='country']").send_keys(country)
            driver.find_element_by_xpath("//*[@id='shipment']").send_keys(last_shipment_date)
            driver.find_element_by_xpath("//*[@id='discharge port']").send_keys(discharge_port)
            driver.find_element_by_xpath("//*[@id='destination port']").send_keys(destination_port)
            driver.find_element_by_xpath("//*[@id='Total Bags']").send_keys(bags)
            driver.find_element_by_xpath("//*[@id='NET WT']").send_keys(NET-WT)
            driver.find_element_by_xpath("//*[@id='GROSS WT']").send_keys(Gross-Wt)
            driver.find_element_by_xpath("//*[@id='CONTAINERS']").send_keys(Containers)
            driver.find_element_by_xpath("//*[@id='RATE']").send_keys(rate)
            driver.find_element_by_xpath("//*[@id='TOTAL VALUE IN WORDS']").send_keys(amount_words)
            driver.find_element_by_xpath("//*[@id='advance']").send_keys(advance)
            driver.find_element_by_xpath("//*[@id='TOTAL VALUE']").send_keys(amount)


           
        elif 'proforma' in query:

            party = input("who is the remitter? ")
            buyer_name = name_dict.get(party)
            buyer_address = address_dict.get(party)
            total_amount = input("what is the amount remitted?")
            amount_words = num2words(total_amount, to = 'currency')
            today = date.today()
            notify_party = input("name of notify party: ")
            dest_country = country_dict.get(party)
            dest_port = input("destination port: ")
            discharge_port = dest_port
            final_dest = dest_country
            advance = input("advance: ")
            payment_terms = advance + "% advance rest against scanned docs"
            date=datetime.datetime.today().strftime('%d%m%Y')
            shipment_date = (today+timedelta(days=18)).strftime('%d-%m-%Y')
            last_shipment_date = (today+timedelta(days=94)).strftime('%d-%m-%Y')
            date_of_contract = (today+timedelta(days= -4)).strftime('%d-%m-%Y')
            date_of_proforma = (today+timedelta(days= -8)).strftime('%d-%m-%Y')
            proforma_invoice_no = str(input("what is the proforma invoice no. ? "))
            containers=float(input("what are the no. of containers? : "))
            bags = (containers * 540)
            bags_wt = float(0.00016)* float(bags)
            gross_wt = int((containers)*(27)) + bags_wt
            net_wt = int((containers*27))
            rate = int(float(total_amount)/float(net_wt))


            PATH = "F:\Drivers\chromedriver.exe"
            driver = webdriver.Chrome(PATH)
            
            driver.get("http://shraddhaimpex.epizy.com/720-2/")

            driver.find_element_by_xpath("//*[@id='main']/div[5]/a[1]").click()

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[3]/div[2]/input").send_keys(proforma_invoice_no)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[3]/div[3]/input").send_keys(date_of_proforma)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[6]/div[2]/input").send_keys(buyer_name)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[6]/div[3]/input").send_keys(buyer_address)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[7]/div[2]/input").send_keys(notify_party)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[9]/div[2]/input").send_keys(dest_country)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[15]/div[2]/input").send_keys(discharge_port)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[16]/div[2]/input").send_keys(final_dest)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[12]/div[2]/input").send_keys(payment_terms)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[12]/div[3]/input").send_keys("On or before", last_shipment_date)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[24]/div[4]/input").send_keys(containers)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[30]/div[2]/input").send_keys(total_amount)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[22]/div[7]/input").send_keys(bags)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[23]/div[2]/input").send_keys(bags)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[23]/div[9]/input").send_keys(net_wt)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[23]/div[10]/input").send_keys(gross_wt)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[24]/div[2]/input").send_keys(net_wt)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[28]/div[1]/input").send_keys(amount_words)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[25]/input").send_keys(rate)

            driver.find_element_by_xpath("//*[@id='pf1']/div[1]/div[26]/div[2]/input").send_keys(total_amount)



        elif 'application' in query:
            party = input("EPC Against which party? : ")
            loan_amount = input("What should be the amount of EPC?:  ")
            loan_amount_words = num2words(loan_amount, lang='en_IN')
            buyer_name = name_dict.get(party)
            buyer_address = address_dict.get(party) 
            country = country_dict.get(party)
            
            date=datetime.datetime.today().strftime('%d%m%Y')
            today = date.today()
            date_1=datetime.datetime.today().strftime('%d-%m-%Y')
            shipment_date = (today+timedelta(days=18)).strftime('%d-%m-%Y')
            last_shipment_date = (today+timedelta(days=94)).strftime('%d-%m-%Y')
            date_of_contract = (today+timedelta(days= -4)).strftime('%d-%m-%Y')

            contract_no = input("Enter Contract Number:  ")
            contract = str("SI/SG/") + str(contract_no) + str("/22-23")

            commodity = "SUGAR"

            hs_code = 17019910

            containers = float(input("How many containers?  "))
            quantity = float(containers*27)
            net_wt = int((containers*27))
            rate = float(input("At what rate?  "))
            total_amount = int(float(rate)*float(net_wt))
            
            if party == "alliance":
                xpath = '//*[@id="main"]/div[6]/a[1]'

            elif party == "mohiddin":
                xpath = '//*[@id="main"]/div[6]/a[1]'

            elif party == 'farlee':
                xpath = '//*[@id="main"]/div[6]/a[1]'

            elif party == 'popular':
                xpath = '//*[@id="main"]/div[6]/a[1]'

            date_string = str(date)

            d1 = date_string[0:1]
            d2 = date_string[1:2]
            m1 = date_string[2:3]
            m2 = date_string[3:4]
            y1 = date_string[4:5]
            y2 = date_string[5:6]
            y3 = date_string[6:7]
            y4 = date_string[7:8]

            PATH = "F:\Drivers\chromedriver.exe"
            driver = webdriver.Chrome(PATH)
            url ="http://shraddhaimpex.epizy.com/720-2/"
  

            new_url = "http://shraddhaimpex.epizy.com/720-2/"
   
            driver.get("http://shraddhaimpex.epizy.com/720-2/")

            driver.find_element_by_xpath("//*[@id='main']/div[1]/a[1]").click()

            driver.find_element_by_xpath("//*[@id='date_1']").send_keys(date_1)

            driver.find_element_by_xpath('//*[@id="PurchaseOrder"]').send_keys(contract)

            driver.find_element_by_xpath('//*[@id="ContractDate"]').send_keys(date_of_contract)

            driver.find_element_by_xpath('//*[@id="LoanAmountWords"]').send_keys(loan_amount_words)

            driver.find_element_by_xpath('//*[@id="LoanAmount"]').send_keys(loan_amount)

            driver.find_element_by_xpath('//*[@id="pf1"]/div[1]/div[36]/input').send_keys(last_shipment_date)

            driver.find_element_by_xpath('//*[@id="Country"]').send_keys(country)

            driver.find_element_by_xpath('//*[@id="BuyerName"]').send_keys(buyer_name)

            driver.find_element_by_xpath('//*[@id="BuyerAddress"]').send_keys(buyer_address)

            driver.find_element_by_xpath('//*[@id="Amount"]').send_keys(loan_amount)

            driver.find_element_by_xpath('//*[@id="D1"]').send_keys(d1)

            driver.find_element_by_xpath('//*[@id="D2"]').send_keys(d2)

            driver.find_element_by_xpath('//*[@id="M1"]').send_keys(m1)

            driver.find_element_by_xpath('//*[@id="M2"]').send_keys(m2)

            driver.find_element_by_xpath('//*[@id="Y1"]').send_keys(y1)

            driver.find_element_by_xpath('//*[@id="Y2"]').send_keys(y2)

            driver.find_element_by_xpath('//*[@id="Y3"]').send_keys(y3)

            driver.find_element_by_xpath('//*[@id="Y4"]').send_keys(y4)

            driver.find_element_by_xpath('//*[@id="2D1"]').send_keys(d1)

            driver.find_element_by_xpath('//*[@id="2D2"]').send_keys(d2)

            driver.find_element_by_xpath('//*[@id="2M1"]').send_keys(m1)

            driver.find_element_by_xpath('//*[@id="2M2"]').send_keys(m2)

            driver.find_element_by_xpath('//*[@id="2Y1"]').send_keys(y1)

            driver.find_element_by_xpath('//*[@id="2Y2"]').send_keys(y2)

            driver.find_element_by_xpath('//*[@id="2Y3"]').send_keys(y3)

            driver.find_element_by_xpath('//*[@id="2Y4"]').send_keys(y4)
        
            driver.execute_script("window.open('');")
  
            # Switch to the new window and open new URL
            driver.switch_to.window(driver.window_handles[1])
            driver.get(new_url)
            driver.find_element_by_xpath(xpath).click()
            driver.find_element_by_xpath('//*[@id="contract"]').send_keys(contract_no)
            driver.find_element_by_xpath('//*[@id="contract_date"]').send_keys(date_of_contract)
            driver.find_element_by_xpath('//*[@id="quantity"]').send_keys(quantity)
            driver.find_element_by_xpath('//*[@id="containers"]').send_keys(containers)
            driver.find_element_by_xpath('//*[@id="rate"]').send_keys(rate)
            driver.find_element_by_xpath('//*[@id="amount"]').send_keys(total_amount)
            driver.find_element_by_xpath('//*[@id="last_date"]').send_keys(last_shipment_date)




            