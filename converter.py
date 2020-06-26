import pandas as pd
import os
import glob
import re
path = "xlsxFiles/*.xlsx"
savePath = "./csvFiles/"
count = 1
for fname in glob.glob(path):
    print(fname)
    xls = pd.ExcelFile(fname)
# print(xls.sheet_names)

    for sheet_name in xls.sheet_names:
        cutName = re.sub('.xlsx', '', fname)
        doubleCutNum = re.sub('xlsxFiles/', '', cutName)
        csvFileName = doubleCutNum + sheet_name
        print(csvFileName)
        data_xls = pd.read_excel(
            fname, sheet_name=sheet_name, dtype=str, index_col=None)
        data_xls.to_csv(savePath + csvFileName + '.csv',
                        encoding='utf-8', index=False)

#data_xls = pd.read_excel('test.xlsx', 'Corona CDM', dtype=str, index_col=None)
#data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False)
