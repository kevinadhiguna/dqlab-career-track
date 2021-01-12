import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom order_date menjadi datetime
df["order_date"] = pd.to_datetime(df["order_date"])
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)