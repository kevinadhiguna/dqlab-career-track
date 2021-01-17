print('Korelasi quantity dengan item_price')
print(retail_raw[['quantity', 'item_price']].corr())