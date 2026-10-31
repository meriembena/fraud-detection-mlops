import pandas as pd
df = pd.read_csv('fraud_eda.csv')
print(df.head())
print(df.describe())
