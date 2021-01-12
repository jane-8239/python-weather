from django.db import models

class Taiwan(models.Model):
    city = models.CharField(max_length=200)
    def __str__(self):
        return self.city
class Temperature(models.Model):
    yearmonth = models.CharField(max_length=200)
    temp = models.FloatField()
    city = models.CharField(max_length=200)
    def  __str__(self):
        return self.city +" "+str(self.temp)
         
    
    

# Create your models here.
