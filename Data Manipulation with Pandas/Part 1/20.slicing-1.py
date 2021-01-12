import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["customer_id"] == "18055") &
		          (df["product_id"].isin(["P0029", "P0040", "P0041", "P0116", "P0117"]))
				 ]
print("Slice langsung berdasarkan kolom:\n", df_slice)