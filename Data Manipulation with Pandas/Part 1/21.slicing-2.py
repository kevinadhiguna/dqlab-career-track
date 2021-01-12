import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Set index dari df sesuai instruksi
df = df.set_index(["order_date", "order_id", "product_id"])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01", 1612339, ["P2154", "P2159"]),:]
print("Slice df:\n", df_slice)