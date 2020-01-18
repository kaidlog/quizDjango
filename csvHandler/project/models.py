from django.db import models
import datetime
# Create your models here.

class Person(models.Model):
 schoolClass = models.CharField(max_length=20) # 班級
 className = models.CharField(max_length=20) # 班級名稱
 schoolClassChinese = models.CharField(max_length=20) # 班級名稱1
 seatNumber = models.CharField(max_length=20) # 座號
 studentID = models.CharField(max_length=20) # 學號
 name = models.CharField(max_length=30) # 姓名
 identityCard = models.CharField(max_length=30) # 身分證
 sex = models.CharField(max_length=2)  # 性別
 birth_date = models.CharField(max_length=20) # 出生日期


class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=20)
    timeSunday = models.TimeField(auto_now=False, blank=True,null=True)
    timeSundayEnd = models.TimeField(auto_now=False, blank=True,null=True)

    timeMonday = models.TimeField(auto_now=False, blank=True,null=True)
    timeMondayEnd = models.TimeField(auto_now=False, blank=True,null=True)

    timeTuesday = models.TimeField(auto_now=False, blank=True,null=True)
    timeTuesdayEnd = models.TimeField(auto_now=False, blank=True,null=True)

    timeWedensday = models.TimeField(auto_now=False, blank=True,null=True)
    timeWedensdayEnd = models.TimeField(auto_now=False, blank=True,null=True)

    timeThursday = models.TimeField(auto_now=False, blank=True,null=True)
    timeThursdayEnd = models.TimeField(auto_now=False, blank=True,null=True)

    timeFriday = models.TimeField(auto_now=False, blank=True,null=True)
    timeFridayEnd = models.TimeField(auto_now=False, blank=True,null=True)

    timeSaturday = models.TimeField(auto_now=False, blank=True,null=True)
    timeSaturdayEnd = models.TimeField(auto_now=False, blank=True,null=True)

    # timeMonday = models.CharField(max_length=20)
    # timeTuesday = models.CharField(max_length=20)
    # timeWedensday = models.CharField(max_length=20)
    # timeThursday = models.CharField(max_length=20)
    # timeFriday = models.CharField(max_length=20)
    # timeSaturday = models.CharField(max_length=20)


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class Feed_Message(models.Model):
    week = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
