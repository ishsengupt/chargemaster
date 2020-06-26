import pandas as pd
import os
import csv
import glob

from pandas.io.parsers import read_csv
import re
path = "csvFiles_copy/*.csv"
savePath = "./csvFiles/"
initialPath = './#2019#&Hollywood Presbyterian Medical Center&106190382_CDM_2019cdmast.190603.csv'

dfinitial = read_csv(initialPath)


for fname in glob.glob(path):
    df = read_csv(fname)
   # print(len(df))
    #count = count + len(df)
    #dfinitial = dfinitial.append(df)
    dfinitial =  pd.concat([dfinitial,df], axis=0, ignore_index=True, sort=True)
    print(dfinitial)

dfinitial.to_csv("sample.csv")
  #  df3 = pd.concat([dfinitial, df], join='outer')
   # print(df3)
    # dfinitial.append(df)
   # dfinitial.to_csv('sample.csv')
# for column in df:
#     if any(x in column for x in ['Price.1']):
#        print(column)
#        print(fname)
#        df.rename(columns={column: 'UNIT_PRICE'}, inplace=True)
#   df.to_csv(fname)

#df1 = read_csv(path1)
#df2 = read_csv(path2)
# print(df1)
# print(df2)
#df3 = df1.append(df2)
#df3 = read_csv("sample.csv")
# print(df3['Hospital'])
