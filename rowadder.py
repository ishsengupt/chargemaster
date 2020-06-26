import pandas
from pandas.io.parsers import read_csv
import csv
import os
import glob
import re

path = "csvFiles/*.csv"

for fname in glob.glob(path):
    df = read_csv(fname)
    print(df)
    result = re.search('#(.*)#', fname)
    result2 = re.search('&(.*)&', fname)
    print(result.group(1))
    print(result2.group(1))
    df['Hospital'] = result2.group(1)
    df['Year'] = result.group(1)

    df.to_csv(fname)
