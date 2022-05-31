import re
import requests
import pdfplumber
import pandas as pd
import os
import openpyxl


wb = openpyxl.load_workbook("ZION.xlsx")
ws_irex = wb['IREX']
ws_irex_pci = wb['IREX-PCI']


### Worksheet IREX 
for cell in ws_irex['A']:
    if cell.value is None:
        row_no = str(cell.row)
        break
tab = cell.row+1
fillcell = str("A")+str(cell.row+1)
ws_irex[str(fillcell)] = "S_"+ str(cell.row)

def data_enter_irex(col, var):
    for cell in ws_irex['A']:
        if cell.value is None:   
            row_no = str(cell.row)
            break
    cell_spec = str(col) + str(cell.row)
    ws_irex[str(cell_spec)] = str(var)
    wb.save("ZION.xlsx")


### Worksheet IREX_PCI
#for cell in ws_irex_pci['A']:
#   if cell.value is None:
#        row_no = str(cell.row)
#        break
#tab = cell.row+1
#fillcell = str("A")+str(cell.row+1)
#s_irex_pci[str(fillcell)] = "S_"+ str(cell.row)

def data_enter_pci(col, var):
    for cell in ws_irex_pci['A']:
        if cell.value is None:
            row_no = str(cell.row)
            break
    tab = cell.row+1
    fillcell = str("A")+str(cell.row+1)
    ws_irex_pci[str(fillcell)] = "S_"+ str(cell.row)


    for cell in ws_irex_pci[col]:
        if cell.value is None:
            row_no = str(cell.row)
            break
    cell_spec = str(col) + str(cell.row)
    ws_irex_pci[str(cell_spec)] = str(var)
    wb.save("ZION.xlsx")



#fullpath = os.path.join("C:/Users/HP/ZION/Web_Apps/Web_App_1/webapp_1/static/pdf_files/Advice-0500IREX10483121.pdf")
#open the advice copy
with pdfplumber.open("C:/Users/HP/ZION/Web_Apps/Web_App_1/webapp_1/static/pdf_files/0500IREX24172821_4.pdf") as irex_pdf:
    page = irex_pdf.pages[0]
    text = page.extract_text()
    
#print(text)

#get irex number
irex_ref = re.compile(r'0500IREX\d{8}')
matches = irex_ref.finditer(text)

for match in matches:
    irex_no = match.group(0)
    #print(match.group(0))

#get PCI number
pci_ref = re.compile(r"^3174PCI.*")
matches = pci_ref.finditer(text)

for match in matches:
    pci_no = match.groups()
    #print(match.group(0))
    #print(pci_no)
    
#get PCI Number - longer approach
pci_refs = re.compile(r'3174PCI\d+\s\d+\s\w+.\w+.\w+.\w+')
matches = pci_refs.finditer(text)

for match in matches:
    pci_details = match.group(0)
    #print(match.group(0))
# print(match)
    #print(pci_details)
    

#get remitter name
remitter = re.compile(r'REMITTERNAME\s\w+')
matches = remitter.finditer(text)

for match in matches:
    remitter = match.group(0)
    #print(match.group(0))
    remitter_name = remitter.replace("REMITTERNAME", "")

#get value date
valuedate = re.compile(r'VALUEDATE\s\d{2}(/)\d{2}(/)\d{4}')
matches = valuedate.finditer(text)

for match in matches:
    date = match.group(0)
    #print(match.group(0))
    value_date = date.replace("VALUEDATE ", "")


amount_inr = re.compile(r'USD\s\d+.+')
matches = amount_inr.finditer(text)

for match in matches:
    amt_1=match.group(0)
    #print(match.group(0))

fc, amt_fc, rate, inr, amt_inr  = amt_1.split(" ")


col_dict = {1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G"}

pci_mat = re.findall( '3174PCI\d+\s\d+\s\w+.\w+.\w+.\w+', text)
print(pci_mat)
index = range(1,7)
length = len(pci_mat)
iter_range = range(0, len(pci_mat))

for i in iter_range:
    pc_elem = str(pci_mat[i])
    print(pc_elem)
    
    pc_no, pc_acc, remb_amt = pc_elem.split(" ")
    print(pc_no, remb_amt)
    data_enter_pci("B", irex_no)
    data_enter_pci("C", value_date)
    data_enter_pci("D", amt_inr)
    data_enter_pci("E", pc_no)
    data_enter_pci("F", remb_amt)




#print(pci_details)
#print(irex_no, amt_fc, rate, amt_inr, pc_no, value_date, remitter, pci_details)


var_dict = {1:irex_no, 2:value_date, 3:amt_fc, 4:rate, 5:amt_inr, 6:remitter_name}
var_pci_dict = {1:irex_no, 2:value_date, 3:amt_inr, 4:pc_no, 5:remb_amt, 6:remitter}

#for i in index:
#    data_enter_irex(col_dict.get(i), var_dict.get(i))

#for i in index:
#    data_enter_pci(col_dict.get(i), var_pci_dict.get(i))

wb.save("ZION.xlsx")  

