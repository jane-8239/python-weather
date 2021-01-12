import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
django.setup()

from mysite.models import Temperature

data_date=list()
data_temperature=list()
with open("Chiayidata.txt","r") as fp:
    txtfile = fp.readlines()
for i in txtfile:
    date,temp=i.split(",")
    data_date.append(date)
    data_temperature.append(temp.strip())
    

    