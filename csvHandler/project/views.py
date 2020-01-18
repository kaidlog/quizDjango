from django.shortcuts import render, redirect
from .models import Restaurant, City,Feed_Message
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate

import requests
from .forms import CityForm, RestaurantForm

# Create your views here.

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

def listone(request):
    # try:
    #     i =1
    #     unit = Restaurant.objects.exclude(timeSunday = 'Closed')[i] #讀取第一筆資料
    #
    #
    #
    # except:
    #     errormessage = "(讀取錯誤!)"
    return render(request,'base.html',locals())


def listall(request):
     # if request.method == 'POST':
     #    form = RestaurantForm(request.POST)
     #    if form.is_valid():
     #        new_week = form.cleaned_data['week']
     #        new_day = form.cleaned_data['day']
     #        # new_week = "Sunday"
     #        upperbound = 'time' + new_week + '__gte'
     #        lowerbound = 'time' + new_week + '__lte'
     #        # print(upperbound)
     # title = Restaurant.objects.last()
     #
     #        Restaurants = Restaurant.objects.all() #依據id欄位遞減排序顯示所有資料
     #        # ttts = Restaurant.objects.filter(timeSunday__gt ='09:00',timeSunday__lt ='11:00').all()
     #        ttts = Restaurant.objects.filter(upperbound = new_day, lowerbound = new_day).all()
     # ttts = ttts.objects.filter(timeSunday__lt ='23:00').all()
     #        #ttt = Restaurant.objects.filter(timeSunday__GT = 1000).all()
     return render(request,'heyhey.html',locals())

def listall_post(request):
    # if request.method == 'POST':
    # form = RestaurantForm(request.POST)
    # print(form)
    # if form.is_valid():
    new_week = request.POST['week']
    # new_day = request.POST['day']
    new_datetimes = request.POST['datetimes']
    print(new_datetimes[6:10])
    print(new_datetimes[21:26])
    # new_week = "Sunday"
    print(new_week)
    # print(new_day)
    # upperbound = 'time' + new_week + '__gte'
    # lowerbound = 'time' + new_week + '__lte'
    # print(upperbound)
    title = Restaurant.objects.last()

    Restaurants = Restaurant.objects.all() #依據id欄位遞減排序顯示所有資料
    # ttts = Restaurant.objects.filter(timeSunday__gt ='09:00',timeSunday__lt ='11:00').all()
    # ttts = Restaurant.objects.filter(upperbound = new_day, lowerbound = new_day).all()
    # print(tt)
    # ttts = ttts.objects.filter(timeSunday__lt ='23:00').all()
    #ttt = Restaurant.objects.filter(timeSunday__GT = 1000).all()
    if new_week == 'Sunday':
        # ttts = Restaurant.objects.filter(timeSunday__gte = new_day,timeSunday__lte = new_day).all()
        ttts = Restaurant.objects.filter(timeSunday__gte = new_datetimes[5:9],timeSunday__lte = new_datetimes[22:26]).all()

        # ttts = Restaurant.objects.filter(timeSunday__gte = new_day,timeSunday__lte = new_datetimes[21:26]).all()
    if new_week == 'Monday':
        ttts = Restaurant.objects.filter(timeSunday__gte = new_datetimes[5:9],timeSunday__lte = new_datetimes[22:26]).all()
    if new_week == 'Tuesday':
        ttts = Restaurant.objects.filter(timeSunday__gte = new_datetimes[5:9],timeSunday__lte = new_datetimes[22:26]).all()
    if new_week == 'Wedensday':
        ttts = Restaurant.objects.filter(timeSunday__gte = new_datetimes[5:9],timeSunday__lte = new_datetimes[22:26]).all()
    if new_week == 'Thursday':
        ttts = Restaurant.objects.filter(timeSunday__gte = new_datetimes[5:9],timeSunday__lte = new_datetimes[22:26]).all()
    if new_week == 'Friday':
        ttts = Restaurant.objects.filter(timeSunday__gte = new_datetimes[5:9],timeSunday__lte = new_datetimes[22:26]).all()
    if new_week == 'Saturday':
        ttts = Restaurant.objects.filter(timeSunday__gte = new_datetimes[5:9],timeSunday__lte = new_datetimes[22:26]).all()
    else:
        pass

    print(ttts[0])

    return render(request,'heyhey.html',locals())

#
#
# def rindex(request):
#     err_msg = ''
#     message = ''
#     message_class = ''
#
#     if request.method == 'POST':
#         form = RestaurantForm(request.POST)
#
#         if form.is_valid():
#             new_day = form.cleaned_data['day']
#             new_time = form.cleaned_data['time']
#
#             if new_day == sunday:
#                 ffff = Restaurant.objects.filter(timeSunday)
#
#             if new_day == monday:
#
#             if new_day == tuesday:
#
#             if new_day == wedensday:
#
#             if new_day == thursday:
#
#             if new_day == friday:
#
#             if new_day == saturday:





def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : message,
        'message_class' : message_class
    }

    return render(request, 'weather/weather.html', context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')

def post_signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(username,email,password)
    if user:
        return redirect('/',locals())
    else:
        return redirect('/signup',locals())

def get_login(request):
    return render(request, 'registration/login.html')
def get_logout(request):
    return render(request, 'logout.html')

def post_logout(request):
    auth.logout(request)
    return redirect('/')


def post_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username = username,password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/',locals())
    else: #帳密錯
        return redirect('/',locals())
def get_signup(request):
    return render(request, 'signup.html')
