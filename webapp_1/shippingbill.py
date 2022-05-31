import re
import requests
import pdfplumber
import pandas as pd
import os
import openpyxl


#fullpath = os.path.join("E:/Shraddha IMPEX/advices/IREX", filename)

with pdfplumber.open("E:/Shraddha IMPEX/Shipping Bills/21-22/LEO/SI92.pdf") as pdf:
    page1 = pdf.pages[0]
    page2 = pdf.pages[1]
    text1 = page1.extract_text()
    text2 = page2.extract_text()

wb = openpyxl.load_workbook("C:/Users/HP/ZION/Web_Apps/Web_App_1/webapp_1/ZION.xlsx")
ws_shipping = wb['SB']


for cell in ws_shipping['A']:
    if cell.value is None:
        row_no = str(cell.row)
        break
fillcell = str("A") + str(cell.row+1)
ws_shipping[str(fillcell)] = "S_" + str(cell.row)

def data_enter_sb(col, var):
    for cell in ws_shipping[col]:
        if cell.value is None:
            row_no=str(cell.row)
            break
    cell_spec = str(col) + str(cell.row)
    ws_shipping[str(cell_spec)] = str(var)
    wb.save("ZION.xlsx")




#df = pd.read_excel (r'SI92.xlsx')

#df.drop_duplicates()
##print(df.to_string())
##print(text1)
##print(text2)



#Notify Party
notify = re.compile(r'SHRADDHA IMPEX.+')
matches = notify.finditer(text2)

for match in matches:
    notify_party = match.group(0)
    #print(match.group(0))
    notifyparty = notify_party.replace("SHRADDHA IMPEX ", '')
    #print(notifyparty)

#Invoice No. 
invoice_details = re.compile(r' SI.+USD')
matches = invoice_details.finditer(text1)

for match in matches:
    invoice = match.group(0)
    tag, invoiceno, giv, tag2 = invoice.split(" ")
    #print(match.group(0))
    
#print(invoiceno, "\n", giv)

#Package No, Gross Wt, Shipping Bill No
grs_wt = re.compile(r'PKG\s.+')
matches = grs_wt.finditer(text1)

for match in matches:
    gross_wt = match.group(0)
    pkg, pkg_no, gwt, mt, grosswt, SB_No = gross_wt.split(" ")
    #print(match.group(0))
#print(pkg_no, "\n", grosswt, "\n", SB_No)


#Leo Date
leodt = re.compile(r'LEO Date.+')
matches = leodt.finditer(text1)
for match in matches:
    leodate = match.group(0)
    tag3, tag4, LEO_Date = leodate.split(" ")
    #print(match.group(0))

#print(LEO_Date)

#Consignee
consignee = re.compile(r'SHRADDHA.+')
matches = consignee.finditer(text1)
for match in matches:
    #print(match.group(0))
    cnsgni = match.group(0)
    consignee_name = cnsgni.replace("SHRADDHA IMPEX ", '')
    #print(consignee_name)

#Invoice Date
invoicedate = re.compile(r'SI.+\s\d{2}.\d{2}.\d{4}')
matches = invoicedate.finditer(text2)
for match in matches:
    #print(match.group(0))
    invdttag = match.group(0)
    tag5, invoice_date = invdttag.split(" ")
    
#print(tag, invoice_date)
#Manufacturer
mfger = re.compile(r"MAEQ QUOTA\s.+")
matches = mfger.finditer(text2)
for match in matches:
    mfg = match.group(0)
    #print(match.group(0))
#HS Code

hscode = re.compile(r'1\s\d{8}')
matches = hscode.finditer(text2)
for match in matches:
    #print(match.group(0))
    hs = match.group(0)
    tag5, hs_code = hs.split(" ")
    #print(hs_code)
#Mfg invoice no. 
splrinv = re.compile(r"s(/)2021(-)22(/)\d{4}")
matches = splrinv.finditer(text2)
for match in matches:
    mfginv = match.group(0)


#Destination 
discharge_country = re.compile(r'COUNTRY OF DISCHARGE\s.+')
matches = discharge_country.finditer(text1)
for match in matches:
    ##print(match.group(0))
    country = match.group(0)
    country_of_discharge = country.replace("COUNTRY OF DISCHARGE ", "")
    ##print(country_of_discharge)
    
#Dest Port
destport = re.compile(r'PORT OF FINAL DESTINATION\s.+')
matches = destport.finditer(text1)
for match in matches:
    ##print(match.group(0))
    portofdest = match.group(0)
    destination_port = portofdest.replace("PORT OF FINAL DESTINATION ", "")
    ##print(destination_port)


sb_dict = {1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K"}
sb_var_dict = {1:SB_No, 2:invoiceno, 3:invoice_date, 4:giv, 5:consignee_name, 6:notifyparty, 7:LEO_Date, 8:hs_code, 9:grosswt, 10:pkg_no}


#for i in range(1, 11):
#    data_enter_sb(sb_dict.get(i) , sb_var_dict.get(i))

#print("Data Entry Successful")

#wb.save("ZION.xlsx")