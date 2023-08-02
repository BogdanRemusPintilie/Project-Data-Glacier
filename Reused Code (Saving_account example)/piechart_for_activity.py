import matplotlib.pylab as plt

data = [65, 24]
labels = ['Active Customers', 'Inactive Customers']


plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)


plt.title('Activity Index')


plt.axis('equal')


plt.show()