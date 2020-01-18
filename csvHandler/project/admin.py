from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Person, Restaurant

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
 list_display = ('id', 'schoolClass', 'className', 'schoolClassChinese', 'seatNumber', 'studentID', 'name', 'identityCard', 'sex', 'birth_date')



 @admin.register(Restaurant)
 class RestaurantAdmin(ImportExportModelAdmin):
  list_display = (
  'id', 'restaurantName', 'timeSunday','timeMonday', 'timeTuesday', 'timeWedensday', 'timeThursday', 'timeFriday', 'timeSaturday',
  'timeSundayEnd','timeMondayEnd','timeTuesdayEnd','timeWedensdayEnd','timeThursdayEnd','timeFridayEnd','timeSaturdayEnd')
