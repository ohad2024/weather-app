import requests
from dataclasses import dataclass

API_key = "API_key"

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    day_temperature: float
    night_temperature: float


def get_lan_lon(city_name, API_key):
    resp = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}").json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon


def get_current_weather(lat, lon, API_key):
    cityid = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}").json()
    id1 = cityid.get('id')
    print(id1)
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={API_key}&units=metric').json()
    daily_data = resp['daily'][0:7]
    daily_weather = []
    for day in daily_data:
        daily_weather.append(WeatherData(
            main=day['weather'][0]['main'],
            description=day['weather'][0]['description'],
            icon=day['weather'][0]['icon'],
            day_temperature=day['temp']['day'],
            night_temperature=day['temp']['night']
        ))

    return daily_weather, id1


def main(city_name):
    lat, lon = get_lan_lon(city_name, API_key)
    daily_weather, id1 = get_current_weather(lat, lon, API_key)
    return daily_weather, id1


if __name__ == "__main__":
    city_name = 'Tel Aviv'
    daily_weather, id1 = main(city_name)
    print("\n8 Days Forecast:")
    for i, day_weather in enumerate(daily_weather, 1):
        print(f"\nDay {i}:")
        print(day_weather)
