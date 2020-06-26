import pandas as pd
import os
import csv
import glob

from pandas.io.parsers import read_csv
import re
pd.options.display.max_rows = 999

df = read_csv("new_sample.csv")
#count = 1

#df['CDM'].astype(str)
#df['CDM'].fillna('0', inplace=True)
#print(df['CDM'])
#df['CDM Code'].astype(str)
#df['CDM Code'].fillna('0', inplace=True)
#df['CDM Number'].astype(str)
#df['CDM Number'].fillna('0', inplace=True)
#df['CDM Number / CDM Code'] =df[['CDM Number','CDM Code', 'CDM']].astype(str).apply(''.join,1)
#df.to_csv("new_sample.csv")
# for column in df.columns:
#    print(count)
#    print(column)
#   print(df[column].dtypes)
#   count = count + 1
#   if df[column].isnull().sum() > 1000000:
#       print('waa')

# if df[column].isnull().sum() > 1000000:
#   print(df[column].isnull().sum())
#   print(column)
#  del df[column]
# df.to_csv("other_sample.csv")
