import glob
path = "xlsxFiles/*.xlsx"
for fname in glob.glob(path):
    print(fname)
