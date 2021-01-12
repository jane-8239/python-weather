from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Temperature,Taiwan
from datetime import datetime
from django.db.models import Avg, Max, Min, Sum
# Create your views here.

def  index(request):
    now=datetime.now()
    return render(request, 'index.html', locals())
def  temp(request):
    return render(request, 'temp.html', locals())
def  city(request,cityName=""):
    now=datetime.now()
    if (cityName != "" ):
        data =Temperature.objects.filter(city = cityName,yearmonth__startswith='2015')
        data2 =Temperature.objects.filter(city = cityName,yearmonth__startswith='2016')
        data3=Temperature.objects.filter(city = cityName,yearmonth__startswith='2017')
    return render(request, 'city.html', locals())
def highlow(request,year=0):
    now=datetime.now()
    high =Temperature.objects.filter(yearmonth__startswith=year)
    high_temp = high.order_by('-temp')[0]
    low = high.order_by('temp')[0]
    return render(request,'highlow.html',locals())

    