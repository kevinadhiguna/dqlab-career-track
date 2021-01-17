dataset_corr = dataset.corr()
print('Korelasi dataset:\n', dataset.corr())
print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())
# Tugas praktek
print('\nKorelasi BounceRates-ExitRates: ', dataset_corr.loc['BounceRates', 'ExitRates'])
print('\nKorelasi Revenue-PageValues: ', dataset_corr.loc['Revenue', 'PageValues'])
print('\nKorelasi TrafficType-Weekend: ', dataset_corr.loc['TrafficType', 'Weekend'])