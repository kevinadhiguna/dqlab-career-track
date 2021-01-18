import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.hist(data_per_customer['quantity'], bins=100, range=(1, 200), color='brown')
plt.title('Distribution of Total Quantity per Customer\nDKI Jakarta in Q4 2019', fontsize=15, color='blue')
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xlim(xmin=0, xmax=200)
plt.show()