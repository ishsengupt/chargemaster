import csv
import pandas
from pandas.io.parsers import read_csv

df = read_csv('CDM.csv')
df1 = df.iloc[:, 0:4]
df1.fillna(0, inplace=True)
df1.to_csv('empty-columns-removed.csv')
print(df1)
