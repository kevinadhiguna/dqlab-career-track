import pandas as pd
# Load data https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv')
# Create variabel pollutant 
pollutant = gaq[['country','city','pollutant','value']].pivot_table(index=['country','city'],columns='pollutant').fillna(0)
# Create sebuah function: iqr
def iqr(series):
	Q1 = series.quantile(0.25)
	Q3 = series.quantile(0.75)
	return Q3 - Q1
# Group berdasarkan country dan terapkan aggregasi dari function: iqr
custom_agg = pollutant.groupby('country').agg(iqr)
print('Custom aggregation (5 teratas):\n', custom_agg.head())