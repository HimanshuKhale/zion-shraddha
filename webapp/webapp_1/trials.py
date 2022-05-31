from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from num2words import num2words
import datetime
from datetime import date, timedelta

party = "alliance"



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


buyer = name_dict.get(party)
buyer_address = address_dict.get(party)
print(buyer, buyer_address)

today = datetime.datetime.today().strftime('%d%m%Y')

#D1 = str(today[1])

#print(D1)
#sample_str=str(today)
#first_chars = sample_str[0:8]
#print('First 3 characters: ', first_chars)

date_string = str(today)

d1 = date_string[0:1]
d2 = date_string[1:2]
m1 = date_string[2:3]
m2 = date_string[3:4]
y1 = date_string[4:5]
y2 = date_string[5:6]
y3 = date_string[6:7]
y4 = date_string[7:8]

#print(d1, d2, m1, m2, y1, y2, y3, y4)

#loan_amount = input("type any number: ")
#loan_amount_words_1 = num2words(loan_amount, to = 'currency')
#loan_amount_words_2 = num2words(loan_amount, lang='en_IN')
#loan_amount_words_3 = num2words(loan_amount, to = 'currency', lang='en_IN')

#print(loan_amount_words_1,   
#loan_amount_words_2, 
#loan_amount_words_3,
#loan_amount)


#contract_no = input("whats contract no")
#contract = str("SI/SG/") + str(contract_no) + str("/22-23")
#print(contract)

#containers = float(input("How many containers?  "))
#quantity = float(containers*27)
#net_wt = int((containers*27))
#rate = float(input("At what rate?  "))
#total_amount = int(float(rate)*float(net_wt))

#print(quantity, net_wt, rate, total_amount)

amt_1 = "USD 66,724.25 74.99 INR5,003,652.00"

fc, amt_fc, rate, amt_inr  = amt_1.split(" ")

print(fc, amt_fc, rate, amt_inr)