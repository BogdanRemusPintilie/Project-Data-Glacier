import pandas

df=pandas.read_csv('C:\\Users\\Bogdan\\Desktop\\Data Glacier\\Saving_Account\\Saving_Account.csv')

variable = df['segmento'].unique()

print (variable)

series=df['segmento'].value_counts()

print(series)