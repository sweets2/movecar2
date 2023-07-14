
import json
from datetime import datetime, timedelta
import requests
from config import get_openweathermap_api_key


FORECAST_FILE = "weather_forecast.json"
API_KEY = get_openweathermap_api_key()
CITY = "Hoboken"
UNITS = "imperial"


def get_weather_forecast():
    """ Simple API request to pull data based on city. Outputs data as JSON file."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&units={UNITS}&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.Timeout:
        print("openweathermap API timed out")

    with open(FORECAST_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    return data

def check_thunderstorm_forecast():
    """If there is any moderate to heavy rain, checks for keywords
    from openweathermap API data for more than a minor amount of rain."""
    with open(FORECAST_FILE, 'r', encoding='utf-8') as file:
        weather_data = json.load(file)

    tomorrow = datetime.now().date() + timedelta(days=1)
    target_date = tomorrow.strftime("%Y-%m-%d")

    moderate_rain = ['moderate', 'light','clear']
    heavy_rain = ['heavy', 'thunderstorm', 'extreme']

    moderate_rain_time = []
    heavy_rain_time = []

    for forecast in weather_data['list']:
        forecast_date = datetime.fromtimestamp(forecast['dt']).date()
        if forecast_date.strftime("%Y-%m-%d") == target_date:
            for word in moderate_rain:
                if word in forecast['weather'][0]['description']:
                    moderate_rain_time.append(forecast["dt_txt"])
            for word in heavy_rain:
                if word in forecast['weather'][0]['description']:
                    heavy_rain_time.append(forecast["dt_txt"])
    print(moderate_rain_time)
    print(heavy_rain_time)
    return moderate_rain_time
