import pandas as pd

df = pd.read_csv("extracted_vim.txt")

df = df.drop_duplicates()
print(df)

df.to_csv(r'pandas_dropped_duplicates.txt', header=None, index=None, sep=' ', mode='a')