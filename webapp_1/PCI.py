import re
import requests
import pdfplumber
import pandas as pd
import os
import openpyxl


wb = openpyxl.load_workbook("ZION.xlsx")
ws_irex = wb['IREX']
ws_irex_pci = wb['IREX-PCI']
ws_epc = wb['PCS']



### Worksheet EPC and data entry function

for cell in ws_epc['A']:
    if cell.value is None:
        row_no = str(cell.row)
        break
tab = cell.row+1
fillcell = str("A")+str(cell.row+1)
ws_epc[str(fillcell)] = "S_"+ str(cell.row)

def data_enter_epc(col, var):
    for cell in ws_epc['A']:
        if cell.value is None:   
            row_no = str(cell.row)
            break
    cell_spec = str(col) + str(cell.row)
    ws_epc[str(cell_spec)] = str(var)
    wb.save("ZION.xlsx")

with pdfplumber.open("E:/Shraddha IMPEX/advices/PCI/Advice-3174PCI002550621.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

#print(text)

pattern = re.compile(r'3174PCI\d{9}')
matches = pattern.finditer(text)

for match in matches:
    EPC_no = match.group(0)
    #print(match.group(0))

disb_date = re.compile(r'DisbursementDate\s\d+.+')
matches = disb_date.finditer(text)

for match in matches:
    date_disb = match.group(0)
    tag, date = date_disb.split(" ")
    
    #print(match.group(0))

po = re.compile(r'SI/\w+.+')
matches = po.finditer(text)

for match in matches:
    agreement_no = match.group(0)
    #print(match.group(0))

buyer = re.compile(r'OverseasBuyerName\s\w+.+')
matches = buyer.finditer(text)

for match in matches:
    buyer_det = match.group(0)
    tag, buyer = buyer_det.split(" ")
    #print(match.group(0))

EPC_details = re.compile(r'\d{2}.\d{2}.\d{4}\s\d{2}.\d{2}.\d{4}\s\w+.+')
matches = EPC_details.finditer(text)

for match in matches:
    epc_det = match.group(0)
    disbursedate, DueDate, Tenure, Amount, Interest = epc_det.split(" ")
    #print(match.group(0))


epc_dict = {1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I"}
epc_var_dict = {1:EPC_no, 2:date, 3:agreement_no, 4:DueDate, 5:Tenure, 6:buyer, 7:Amount, 8:Interest}


for i in range(1,9):
    data_enter_epc(epc_dict.get(i), epc_var_dict.get(i))


print(EPC_no)
print(date)
print(agreement_no)
print(buyer)
print(DueDate)
print(Tenure)
print(Amount)
print(Interest)
