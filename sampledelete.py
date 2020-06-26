
from pandas.io.parsers import read_csv
import csv
import os
import glob
import re
import numpy as np
import pandas as pd
fname = "test_sample.csv"

df = read_csv(fname)

#del df['CDM']
#del df['CDM Code']
#del df['CDM Number']

# df.to_csv(fname)

# for i in range(len(df.columns)):
#  if "Unnamed" in df.columns[i]:
for column in df.columns:
    #df[column].astype(str)
    #df[column].fillna('0', inplace=True)
     if "Unnamed" in column:
       print(column)
       del df[column]
df.to_csv("test_sample.csv")
