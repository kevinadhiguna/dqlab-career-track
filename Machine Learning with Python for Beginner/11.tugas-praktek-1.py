import matplotlib.pyplot as plt
# visualizing the distribution of customers around the Region
plt.hist(dataset['region'], color = 'lightblue')
plt.title('Distribution of Customers', fontsize = 20)
plt.xlabel('Region Codes', fontsize = 14)
plt.ylabel('Count Users', fontsize = 14)
plt.show()
