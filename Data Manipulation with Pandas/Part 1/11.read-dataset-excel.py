import pandas as pd
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_excel.xlsx", sheet_name="test")
print(df_excel.head(4)) # Menampilkan 4 data teratas