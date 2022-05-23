from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from num2words import num2words
import datetime
from datetime import date, timedelta




buyer_name =input("who is the remitter?")
buyer_address = input("what is the address?")
total_amount = input("what is the amount remitted?")
amount_words = num2words(total_amount, to = 'ordinal')
today = date.today()
notify_party = input("name of notify party: ")
dest_country = input("destination country: ")
dest_port = input("destination port: ")
discharge_port = dest_port
final_dest = dest_port
advance = input("advance: ")
mode = input("scanned copy or through bank")
payment_terms = advance + "% advance balance payment against" + mode
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


