import dotenv
from django.shortcuts import render
import requests
import json

# Create your views here.

dotenv.load_dotenv("/static/.env")
def index(request):

    ip = requests.get('https://api.ipify.org?format=json')
    ip_json = json.loads(ip.text)

    res = requests.get(f'http://ip-api.com/json/{ip_json["ip"]}?lang=en')

    location_text = res.text
    location_json = json.loads(location_text)

    # lat = location_json['lat']
    # lon = location_json['lon']
    #
    #
    # weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={"API_KEY"}')
    # weather_json = json.loads(weather.text)

    
    return render(request, 'index.html', {'data': location_json})


def weather(request):

    lat = index(request).get('lat', None)
    lon = index(request).get('lon', None)
    

    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={"API_KEY"}')

    weather_json = json.loads(weather.text)

    return render(request, 'weather.html', {'data': weather_json})



