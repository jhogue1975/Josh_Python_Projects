import datetime, csv

cr = csv.reader(open("Source.csv", 'rb'))

a =  datetime.datetime.now()
numdays = 1
dateList = []

for x in range(numdays):
    dateList.append(a - datetime.timedelta(days = 15))
    print numdays

for row in cr:
    print row
