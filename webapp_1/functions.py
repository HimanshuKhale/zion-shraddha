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
PATH = "C:/Users/HP/Desktop/Web_App_1/webapp/chromedriver.exe"


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
            'ensen' : 'F 07, PEOPLES PARK SHOPPING COMPLEX, COLOMBO 11, SRILANKA', 
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




def disposal_instructions(party, amount):
    #party = input("who is the remitter? ")
    buyer = name_dict.get(party)
    address = address_dict.get(party)
    #amount = input("what is the amount remitted?")
    amount_words = num2words(amount, lang='en')
    today = date.today()
    today_date=datetime.datetime.today().strftime('%d%m%Y')
    date_today=datetime.datetime.today().strftime('%d%m%Y')
    date_string = str(date_today)

    shipment_date = (today+timedelta(days=18)).strftime('%d%m%Y')
    shipment_string = str(shipment_date)
    last_shipment_date = (today+timedelta(days=94)).strftime('%d%m%Y')
    date_of_contract = (today+timedelta(days= -4)).strftime('%d%m%Y')
    # proforma_invoice_no = input("what is the proforma invoice no. ? ")
    # date_of_proforma = (today+timedelta(days= -8)).strftime('%d-%m-%Y')
    # containers=float(input("what are the no. of containers? : "))
    # bags = (containers * 540)
    # bags_wt = float(0.00016)* float(bags)
    # gross_wt = int((containers)*(27)) + bags_wt
    # net_wt = int((containers*27))
    # rate = int(float(amount)/float(net_wt))

    #notify = input("is there any notify party?  y/n: ")

    # if notify=='y':
    #     notify_party = input("name the notify party")
    # else:
    #     notify_party = buyer
    #     notify_address = address

    d1 = date_string[0:1]
    d2 = date_string[1:2]
    m1 = date_string[2:3]
    m2 = date_string[3:4]
    y1 = date_string[4:5]
    y2 = date_string[5:6]
    y3 = date_string[6:7]
    y4 = date_string[7:8]

    sd1 = shipment_string[0:1]
    sd2 = shipment_string[1:2]
    sm1 = shipment_string[2:3]
    sm2 = shipment_string[3:4]
    sy1 = shipment_string[4:5]
    sy2 = shipment_string[5:6]
    sy3 = shipment_string[6:7]
    sy4 = shipment_string[7:8]

    driver = webdriver.Chrome(PATH)

    

    driver.get("C:/Users/HP/Desktop/Web_App_1/webapp/webapp_1/templates/Disposal_Instructions_Form_Edit_12.html")

    #driver.find_element_by_xpath("//*[@id='main']/div[2]/a[1]").click()

    driver.find_element_by_xpath("//*[@id='amount']").send_keys(amount)
    driver.find_element_by_xpath("//*[@id='amount_words']").send_keys(amount_words)
    driver.find_element_by_xpath("//input[@id='buyer_name']").send_keys(buyer)
    
    driver.find_element_by_xpath("//*[@id='buyer_address']").send_keys(address)
    driver.find_element_by_xpath("//input[@id='d1']").send_keys(sd1)
    driver.find_element_by_xpath("//input[@id='d2']").send_keys(sd2)
    driver.find_element_by_xpath("//*[@id='m1']").send_keys(sm1)
    driver.find_element_by_xpath("//*[@id='m2']").send_keys(sm2)
    driver.find_element_by_xpath("//*[@id='y1']").send_keys(sy1)
    driver.find_element_by_xpath("//*[@id='y2']").send_keys(sy2)
    driver.find_element_by_xpath("//*[@id='y3']").send_keys(sy3)
    driver.find_element_by_xpath("//*[@id='y4']").send_keys(sy4)
    
    driver.find_element_by_id('pg_1_d1').send_keys(d1)
    driver.find_element_by_id('pg_1_d2').send_keys(d2)
    driver.find_element_by_id('pg_1_m1').send_keys(m1)
    driver.find_element_by_id('pg_1_m2').send_keys(m2)
    driver.find_element_by_id('pg_1_y1').send_keys(y1)
    driver.find_element_by_id('pg_1_y2').send_keys(y2)
    driver.find_element_by_id('pg_1_y3').send_keys(y3)
    driver.find_element_by_id('pg_1_y4').send_keys(y4)
   
    #driver.find_element_by_id('pg_2_date').send_keys(d1,"  ",d2, "  ", m1,"  ",m2,"  ",y1,"  ",y2,"  ",y3,"  ",y4)
    driver.find_element_by_id('pg_2_d2').send_keys(d2)
    driver.find_element_by_id('pg_2_m1').send_keys(m1)
    driver.find_element_by_id('pg_2_m2').send_keys(m2)
    
    driver.find_element_by_id('pg_2_y2').send_keys(y2)
    #driver.find_element_by_id('pg_2_y3').send_keys(y3)
    #driver.find_element_by_id('pg_2_y4').send_keys(y4)
    #driver.find_element_by_id('pg_2_y1').send_keys(y1)
    #driver.switch_to.window(driver.window_handles[1])
    # driver.get(new_url)

    # driver.find_element_by_xpath("//*[@id='main']/div[5]/a[1]").click()

    # driver.find_element_by_xpath("//*[@id='Proforma-Invoice-No']").send_keys(proforma_invoice_no)
    # driver.find_element_by_xpath("//*[@id='date']").send_keys(date_of_proforma)
    # driver.find_element_by_xpath("//*[@id='buyer']").send_keys(buyer)
    # driver.find_element_by_xpath("//*[@id='address']").send_keys(address)
    # driver.find_element_by_xpath("//*[@id='notify party']").send_keys(notify_party)
    # driver.find_element_by_xpath("//*[@id='notify party address']").send_keys(notify_address)
    # driver.find_element_by_xpath("//*[@id='country']").send_keys(country)
    # driver.find_element_by_xpath("//*[@id='shipment']").send_keys(last_shipment_date)
    # driver.find_element_by_xpath("//*[@id='discharge port']").send_keys(discharge_port)
    # driver.find_element_by_xpath("//*[@id='destination port']").send_keys(destination_port)
    # driver.find_element_by_xpath("//*[@id='Total Bags']").send_keys(bags)
    # driver.find_element_by_xpath("//*[@id='NET WT']").send_keys(NET-WT)
    # driver.find_element_by_xpath("//*[@id='GROSS WT']").send_keys(Gross-Wt)
    # driver.find_element_by_xpath("//*[@id='CONTAINERS']").send_keys(Containers)
    # driver.find_element_by_xpath("//*[@id='RATE']").send_keys(rate)
    # driver.find_element_by_xpath("//*[@id='TOTAL VALUE IN WORDS']").send_keys(amount_words)
    # driver.find_element_by_xpath("//*[@id='advance']").send_keys(advance)
    # driver.find_element_by_xpath("//*[@id='TOTAL VALUE']").send_keys(amount)

