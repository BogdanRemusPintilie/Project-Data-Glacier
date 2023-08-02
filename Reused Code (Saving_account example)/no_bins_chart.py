import pandas, matplotlib.pyplot as plt

df= pandas.read_csv('C:\\Users\\Bogdan\\Desktop\\Data Glacier\\Saving_Account\\Saving_Account.csv')

canal_counts = df['canal_entrada'].value_counts().sort_values(ascending=False)


plt.figure(figsize=(10, 6))


bar_plot=canal_counts.plot.bar()


plt.xlabel('Channel')
plt.ylabel('Number of Observations')
plt.title('Number of Observations by Channel')


for index, value in enumerate(canal_counts):
    bar_plot.text(index, value, str(value), ha='center', va='bottom')


plt.show()
