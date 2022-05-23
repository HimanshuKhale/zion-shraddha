import os
import re
import requests
import pdfplumber
import pandas as pd
import os
import openpyxl

my_list = []
i=1
wb = openpyxl.load_workbook("ZION data.xlsx")
ws_irex = wb['IREX']
ws_irex_pci = wb['IREX-PCI']

for cell in ws_irex['A']:
    if cell.value is None:
        row_no = str(cell.row)
        break
tab = cell.row+1
fillcell = str("A")+str(cell.row+1)
ws_irex[str(fillcell)] = "S_"+ str(cell.row)

def data_enter(col, var):
    for cell in ws_irex['A']:
        if cell.value is None:   
            row_no = str(cell.row)
            break
    cell_spec = str(col) + str(cell.row)
    ws_irex[str(cell_spec)] = str(var)


# return all files as a list
for file in os.listdir(r'E:/Shraddha IMPEX/advices/IREX'):
	# check the files which are end with specific extension
	if file.endswith(".pdf"):
		
		file_path = os.path.join(r'E:/Shraddha IMPEX/advices/IREX', file)
		print(i, file_path)
		i=i+1
		
		with pdfplumber.open(file_path) as pdf:
			page = pdf.pages[0]
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
			pci_no = match.group(0)
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

#get value date
		valuedate = re.compile(r'VALUEDATE\s\d{2}(/)\d{2}(/)\d{4}')
		matches = valuedate.finditer(text)

		for match in matches:
			value_date = match.group(0)
    #print(match.group(0))


		amount_inr = re.compile(r'USD\s\d+.+')
		matches = amount_inr.finditer(text)

		for match in matches:
			amttext=match.group(0)
    
			fc, amt_fc1, rate1, inr1, amt_inr1  = amttext.split(" ")
		


		pci_mat = re.findall( '3174PCI\d+\s\d+\s\w+.\w+.\w+.\w+', text)
		print(pci_mat)
		index = range(1,7)
		length = len(pci_mat)
		iter_range = range(0, length)
		for i in iter_range:
			pc_elem = str(pci_mat[i])
			pc_no, pc_acc, remb_amt = pc_elem.split(" ")
			print(pc_no, remb_amt)

			
   
		

#print(pci_details)
#print(irex_no, amt_fc, rate, amt_inr, pci_no, value_date, remitter, pci_details)

		col_dict = {1:"B", 2:"C"}#, 3:"D", 4:"E", 5:"F", 6:"G"}
		var_dict = {1:irex_no, 2:value_date}#, 3:amt_fc, 4:rate, 5:amt_inr, 6:remitter}


		for i in range(1-2):
			data_enter(col_dict.get(i), var_dict.get(i))

		wb.save("ZION data.xlsx")  




