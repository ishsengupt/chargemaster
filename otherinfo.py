import pandas as pd
import os
import glob
import re
path = "xlsxFiles/*.xlsx"
savePath = "./csvFiles/"
count = 1
for fname in glob.glob(path):
    # print(fname)
    xls = pd.ExcelFile(fname)

    for sheet_name in xls.sheet_names:
        cutName = re.sub('.xlsx', '', fname)
        doubleCutNum = re.sub('xlsxFiles/', '', cutName)
        csvFileName = doubleCutNum + sheet_name
        print(csvFileName)
