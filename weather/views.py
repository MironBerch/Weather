from django.shortcuts import render
from django.views.generic.base import View
import requests
from .models import City
from .forms import CityForm


def main(request):
    API_KEY = '257d33e204cb72ae037cc13895272f13'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY
        
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
 
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/main.html', context)