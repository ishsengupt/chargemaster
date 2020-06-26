from pandas.io.parsers import read_csv
import csv
import os
import glob
import re
import numpy as np
import pandas as pd

path = "csvFiles/*.csv"
altPath = "csvFiles/#2019#$Marshall Medical Center$106090933_CDM_2019MMC PHARMACY.csv"
df = read_csv(altPath)
df.columns = [*df.columns[:-1], 'PATIENT_PRICE']
df.to_csv(altPath)
#for fname in glob.glob(path):
 #   df = read_csv(fname)
 #   if "Kaiser" in fname:
 #       df.columns = [*df.columns[:-1], 'UNIT_PRICE']
  #  df.to_csv(fname)
