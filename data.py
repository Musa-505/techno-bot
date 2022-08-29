import openpyxl

wb = openpyxl.load_workbook('test6.xlsx')  
sheet = wb.active 
cells = sheet['A1':'B13']  

for i1,i2 in cells:  
    code = ("{0:8} {1:8}".format(i1.value,i2.value))
