import pandas as pd

file = r'F:\project\qin\url_web.csv'

df = pd.read_csv(file)

df_url_web = df.dropna(axis=0).reset_index(drop=True).value_counts()

print(df_url_web)


