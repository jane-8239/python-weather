from django.contrib import admin
from mysite.models import Taiwan,Temperature

# Register your models here.

class TaiwanAdmin(admin.ModelAdmin):
    list_display = ('city',) 
admin.site.register(Taiwan,TaiwanAdmin)
class Temperatureadmin(admin.ModelAdmin):
    list_display = ('yearmonth','temp','city',) 
admin.site.register(Temperature,Temperatureadmin)