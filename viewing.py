import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv ('name.csv', header= None )

df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code']


#print ([df])
#print (df['State',])
#print (df[['State', 'Area Code']])
#print (df['First'][5:10])
#print (df.iloc[1])
#print (df.iloc[2,1])

wanted_values = df[['First', 'Last', 'State']]
stared = wanted_values.to_excel('State_Location.xlsx', index=None)

#save to excel
#df_csv.to_excel('modified.xlsx')
