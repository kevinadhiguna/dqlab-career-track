monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)