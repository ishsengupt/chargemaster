import csv
with open(r"C:\work\DATA\Raw_data\store.csv", 'rb') as f:
    reader = csv.reader(f)
    linenumber = 1
    try:
        for row in reader:
            linenumber += 1
    except Exception as e:
        print(("Error line %d: %s %s" % (linenumber, str(type(e)), e.message)))
