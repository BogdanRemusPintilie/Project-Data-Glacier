import pandas

df = pandas.read_csv('C:\\Users\\Bogdan\\Desktop\\Data Glacier\\Saving_Account\\Train.csv')

df_saving_account=df[df['ind_ahor_fin_ult1']==1 & df['indfall']=='N']

Saving_Account=df_saving_account.drop_duplicates(subset=['ncodpers'], keep='first')

Saving_Account.to_csv('C:\\Users\\Bogdan\\Desktop\\Data Glacier\\Saving_Account\\Saving_Account.csv')