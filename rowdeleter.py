
from pandas.io.parsers import read_csv
import csv
import os
import glob
import re
import numpy as np
import pandas as pd
import scipy.sparse as sp

#x,y = sp.coo_matrix(df.isnull()).nonzero()
#print(list(zip(x,y)))

path = "csvFiles_copy/*.csv"
fname = "other_sample.csv"

# for fname in glob.glob(path):
df = read_csv(fname)
# for i in range(len(df.columns)):
#   if "Unnamed" in df.columns[i]:
for column in df.columns:
    if "CDM" in column:
        print(column)
        # print(df[column].notna().idxmax())
        idx, idy = np.where(pd.isnull(df[column]))
        result = np.column_stack([df[column].index[idx], df[column].columns[idy]])
        print(result)
        #print(df.loc[pd.isna(df[column]), :].index)
        #del df[column]
    # df.to_csv(fname)
        #   print(df.columns[i])
        #print(df.iloc[:, [i]])

    #df1 = df.iloc[:, 3:]
    # print(df1)
    # df1.to_csv(fname)

    # if "Price" not in df.columns:
    #    print(df.columns)
    # for column in df:
    #    if any(x in column for x in ['Outpatient']):
    #       print(column)
    #       print(fname)
    #       df.rename(columns={column: 'Outpatient Price'}, inplace=True)
    #  df.to_csv(fname)
    # for column in df:
    #  if ("Unnamed" in column):
    #      os.unlink(fname)
    #      break
    #  else:
    #      print(df.columns)

    # print(fname)
    # df1.to_csv(fname)
    # print(fname)
    # df1.to_csv(fname)
    # for column in df:
    #    if any(x in column for x in ['Price.1']):
    #        print(column)
    #        print(fname)
    #    df.rename(columns={column: 'UNIT_PRICE'}, inplace=True)
    #       df.to_csv(fname)
