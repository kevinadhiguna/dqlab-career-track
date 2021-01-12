import pandas as pd
# Load dataset https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv', parse_dates=True, index_col='timestamp')
# Cetak 5 data teratas
print(gaq.head())
# Cetak info dari dataframe gaq
print('info')
print(gaq.info())