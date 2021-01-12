import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE','weather.settings')
django.setup()

from mysite.models import Temperature

data_date = []
data_temp = []
data_city = []

for i in range(19):
    with open('temp'+ str(i) +'.csv', newline='', encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile)
        rows.__next__() #略過首行
        for row in rows:
            data_city.append(row[0])
            data_date.append(row[1]+'-'+row[2])
            data_temp.append(row[3])
for i in range(len(data_date)):
    t = Temperature(yearmonth=data_date[i], temp=data_temp[i], city=data_city[i])
    t.save()
print("Done")



