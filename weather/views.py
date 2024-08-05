import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather(city):
    api_key = '50e8d6c7e2a30bca6ba7ba516e6712fd'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def weather_view(request):
    weather_data = None
    error = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather(city)
            if weather_data is None:
                error = "City not found or API request failed."
    else:
        form = CityForm()
    context = {
        'form': form,
        'weather_data': weather_data,
        'error': error,
    }
    return render(request, 'weather/weather.html', context)
