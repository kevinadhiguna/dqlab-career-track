import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep="\t")
# Index dari df
print("Index:", df.index)
# Column dari df
print("Columns:", df.columns)