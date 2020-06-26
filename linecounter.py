import pandas as pd
import os
import glob
import csv
from pandas.io.parsers import read_csv
import re
path = "csvFiles/*.csv"


for fname in glob.glob(path):

    with open(fname) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            pass
        print(csv_reader.line_num)
        if csv_reader.line_num < 500:
            os.unlink(fname)
