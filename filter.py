import pandas as pd 

df = pd.read_csv('name.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

#print (df.loc[df['City'] == 'City 9'])
#print (df.loc[(df['City'] == 'City 9') & (df['First'] == 'Don 9')])

df['Tax %'] = df['Income'].apply(lambda x: .15 if 9999 < x < 39999 else .2 if 40000 < x < 80000 else .25)

df['Taxes Owed'] = df['Income'] * df['Tax %']

to_drop = ['Area Code', 'First', 'Address']
df.drop(columns=to_drop, inplace=True)


df['Test Col'] = False
df.loc[df['Income'] < 60000, 'Test Col'] = True

#print (df['Taxes Owed'])
#print (df.groupby(['Test Col']).mean().sort_values('Income'))

#print (df)
