import pandas as pd

df = pd.read_csv('Math50_Data.csv')
new_df = df.sample(frac=0.01)
new_df.to_csv('Filtered_Math50_Data.csv')
