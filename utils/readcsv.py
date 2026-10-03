
import csv

csvdata = "test_data/cred1.csv"

data=[]

def readdatafromCsv():
    with open (csvdata) as csvfile :
        dataincsv = csv.DictReader(csvfile)
        for row in dataincsv:
            data.append(row)
    return data
    