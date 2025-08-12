import pandas as pd
import matplotlib as mp

file = pd.read_csv('day5.csv')
file.columns = file.columns.str.strip()

print('original data:')
print(file.head())

x = file.groupby('category')['sales'].sum()

print('\n Sales by category')
print(x)

x.plot(kind='bar', title=' sales by category', colour='skyblue')

mp.xlabel('category')
mp.ylabel('sales')
mp.tight_layout()
mp.show()