import pandas as pd
import openpyxl
file_name = 'PL_24_May_2020_TBC_Fidaxomicin_TBC.xlsx'
dfs = pd.read_excel(file_name, sheet_name='General & Costing Assumptions').fillna("")
srcfile = openpyxl.load_workbook('General Costing Assumptions - Template.xlsx',read_only=False, keep_vba= True)
sheetname = srcfile.get_sheet_by_name('Sheet1')
sheetname['A2']= dfs.get('Unnamed: 11')[7].strftime('%Y/%m/%d')
sheetname['B2']= dfs.get('FIDAXOMICIN')[6]
sheetname['C2']= dfs.get('Unnamed: 7')[4]
sheetname['D2']= dfs.get('FIDAXOMICIN')[9]
sheetname['E2']= dfs.get('Unnamed: 2')[45]
sheetname['F2']= dfs.get('Unnamed: 7')[9]*100
sheetname['G2']= dfs.get('Unnamed: 7')[8]*100
sheetname['H2']= dfs.get('Unnamed: 7')[7]
sheetname['I2']= dfs.get('FIDAXOMICIN')[12]*100
sheetname['J2']= dfs.get('FIDAXOMICIN')[8]
sheetname['K2']= dfs.get('FIDAXOMICIN')[10]
sheetname['L2']= dfs.get('Unnamed: 7')[11]*100
sheetname['M2']= dfs.get('Unnamed: 4')[34]
sheetname['N2']= dfs.get('Unnamed: 7')[5]
sheetname['O2']= dfs.get('Unnamed: 7')[14]
sheetname['P2']= dfs.get('Unnamed: 11')[6].strftime('%Y/%m/%d')
sheetname['Q2']= dfs.get('Unnamed: 7')[6]
sheetname['R2']= dfs.get('FIDAXOMICIN')[3]
sheetname['S2']= dfs.get('Unnamed: 7')[15]*100
sheetname['T2']= dfs.get('FIDAXOMICIN')[11]
keys = []
for i in range(84,92):
    if dfs.get('Unnamed: 1')[i]!='':
        keys.append(dfs.get('Unnamed: 1')[i])
for i in range(len(keys)):
    sheetname[f'U{2+i}']=keys[i] 
sheetname['V2']= dfs.get('Unnamed: 7')[12]*100
sizes = []
for i in range(50,65):
    if dfs.get('Unnamed: 2')[i]!='':
        sizes.append(dfs.get('Unnamed: 2')[i])
for i in range(len(sizes)):
    sheetname[f'W{2+i}']=sizes[i] 
sheetname['X2']= dfs.get('FIDAXOMICIN')[13]
sheetname['Y2']= dfs.get('FIDAXOMICIN')[5].strftime('%Y/%m/%d')
sheetname['AA2']= dfs.get('Unnamed: 11')[5].strftime('%Y/%m/%d')
sheetname['AB2']= dfs.get('Unnamed: 7')[10]*100
sheetname['AC2']= dfs.get('Unnamed: 7')[13]*100
sheetname['AD2']= dfs.get('FIDAXOMICIN')[16]
sheetname['AE2']= dfs.get('Unnamed: 14')[0]
srcfile.save('newfile.xlsm')