import os
import glob
import csv
import pandas as pd
path = "csvFiles_copy/*.csv"
count = 0
for fname in glob.glob(path):
    with open(fname) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            pass
        # print(csv_reader.line_num)
        count = csv_reader.line_num + count
        print(count)
       # if csv_reader.line_num < 200:
        #   print(csv_reader.line_num)
        #  os.unlink(fname)
