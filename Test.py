import pandas as pd
from openpyxl import Workbook


df_excel = pd.read_excel ('regions.xlsx')
df_csv = pd.read_csv ('crime.csv' )
#df_csv = pd.read_csv ('crime.csv', header= None )
df_txt = pd.read_csv ('data.txt', delimiter='\t')
df_access = pd.read_sql


#df_csv.columns = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th','11th']
print (df_csv)


#save to excel
#df_csv.to_excel('modified.xlsx')
