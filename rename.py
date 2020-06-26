import csv
import os
import glob
import re

path = "csvFiles/*.csv"

for fname in glob.glob(path):

    os.rename(fname, fname.replace("$", "&"))
