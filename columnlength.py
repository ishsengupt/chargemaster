import pandas as pd
import os
import glob
import csv
from pandas.io.parsers import read_csv
import re
path = "csvFiles/*.csv"


for fname in glob.glob(path):
    df = read_csv(fname)
    print(len(df.columns))
    if (len(df.columns) < 4):
        os.unlink(fname)
