import pandas, matplotlib.pyplot as plt

df= pandas.read_csv('C:\\Users\\Bogdan\\Desktop\\Data Glacier\\Saving_Account\\Saving_Account.csv')

brackets=[0,100000,200000,300000,400000,500000,600000,700000,800000,900000]

df['new_column']=pandas.cut(df['renta'], bins = brackets, right=False)

just_counts = df['new_column'].value_counts()
just_counts=just_counts[just_counts!=0]

plt.bar(just_counts.index.astype(str), just_counts.values)

plt.xlabel('Household income brackets')
plt.ylabel('Observations')
plt.title('Household income distribution')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

for index, value in enumerate(just_counts.values):
        plt.text(index, value, str(value), ha='center', va='bottom')


plt.show()