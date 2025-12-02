import requests
from dotenv import load_dotenv
import os

load_dotenv()
auth_api_weather = os.getenv("auth_api_weather")

# Complete API endpoint for current weather
base_url_current = 'http://api.weatherapi.com/v1/current.json'

def get_api(api_url, auth_api_weather, location):
    """
    Makes a GET request to the specified API URL and returns the JSON response.

    Args:
        api_url (str): The URL of the API endpoint.
        auth_api_weather (str): The authentication key for the API.
        location (str): The location to get weather data for.
    Returns:
        dict: The JSON response from the API.
    """
    
    params = {
        "key": auth_api_weather,
        "q": location
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def mock_get_api():
    return {'location': {'name': 'Jakarta', 'region': 'Jakarta Raya', 'country': 'Indonesia', 'lat': -6.2146, 'lon': 106.8451, 'tz_id': 'Asia/Jakarta', 'localtime_epoch': 1764646901, 'localtime': '2025-12-02 10:41'}, 'current': {'last_updated_epoch': 1764646200, 'last_updated': '2025-12-02 10:30', 'temp_c': 31.3, 'temp_f': 88.3, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 2.2, 'wind_kph': 3.6, 'wind_degree': 227, 'wind_dir': 'SW', 'pressure_mb': 1011.0, 'pressure_in': 29.85, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 71, 'cloud': 50, 'feelslike_c': 38.5, 'feelslike_f': 101.2, 'windchill_c': 28.2, 'windchill_f': 82.7, 'heatindex_c': 31.4, 'heatindex_f': 88.5, 'dewpoint_c': 22.5, 'dewpoint_f': 72.4, 'vis_km': 7.0, 'vis_miles': 4.0, 'uv': 8.9, 'gust_mph': 6.7, 'gust_kph': 10.8, 'short_rad': 394.36, 'diff_rad': 103.25, 'dni': 0.0, 'gti': 103.18}}


