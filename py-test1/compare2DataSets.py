import pandas as pd

# Create two sample dataframes with Indian names
data1 = {
    'Name': ['Aarav', 'Vivaan', 'Aditya'],
    'Age': [25, 30, 35]
}

data2 = {
    'Name': ['Aarav', 'Vivaan', 'Kabir'],
    'Age': [25, 30, 40]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Compare the dataframes
comparison = df1.merge(df2, on='Name', how='outer', suffixes=('_df1', '_df2'), indicator=True)

print("Comparison of DataFrames:")
print(comparison)

