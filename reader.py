import os
import glob
import csv
import pandas as pd
path = "csvFiles/*.csv"
thisDict = {}
for fname in glob.glob(path):
    with open(fname, newline='') as f:
        csv_reader = csv.reader(f)
        csv_headings = next(csv_reader)
       # print(csv_headings)
        for heading in csv_headings:
            if heading in thisDict:
                prevNum = thisDict[heading]
                thisDict[heading] = prevNum + 1
            else:
                thisDict[heading] = 1

print(thisDict)
