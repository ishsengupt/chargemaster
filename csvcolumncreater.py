from pandas.io.parsers import read_csv
import csv
import os
import glob
import re
import numpy as np
import pandas as pd


fname = "test_sample.csv"

df = read_csv(fname)

for column in df.columns:
   # if "Unnamed" in column:
    #    continue
    #column = column.replace("/", "")
   # column = column.replace(" ", "_")

    #print(column + " text,")
