import csv
import os
import glob
import re

path = "csvFiles/*.csv"

for fname in glob.glob(path):

    result = re.search('#(.*)#', fname)
    result2 = re.search('&(.*)&', fname)
    print(result.group(1))
    print(result2.group(1))
