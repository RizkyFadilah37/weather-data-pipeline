import requests
from dotenv import load_dotenv
import os

load_dotenv()
auth_api_weather = os.getenv("auth_api_weather")

# Complete API endpoint for current weather
base_url = 'http://api.weatherapi.com/v1/current.json'

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
    return {'location': {'name': 'Jakarta', 'region': 'Jakarta Raya', 'country': 'Indonesia', 'lat': -6.2146, 'lon': 106.8451, 'tz_id': 'Asia/Jakarta', 'localtime_epoch': 1764678124, 'localtime': '2025-12-02 19:22'}, 'current': {'last_updated_epoch': 1764677700, 'last_updated': '2025-12-02 19:15', 'temp_c': 26.1, 'temp_f': 79.0, 'is_day': 0, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 5.6, 'wind_kph': 9.0, 'wind_degree': 356, 'wind_dir': 'N', 'pressure_mb': 1010.0, 'pressure_in': 29.83, 'precip_mm': 1.56, 'precip_in': 0.06, 'humidity': 84, 'cloud': 25, 'feelslike_c': 27.7, 'feelslike_f': 81.9, 'windchill_c': 29.2, 'windchill_f': 84.5, 'heatindex_c': 32.7, 'heatindex_f': 90.9, 'dewpoint_c': 22.5, 'dewpoint_f': 72.5, 'vis_km': 6.0, 'vis_miles': 3.0, 'uv': 0.0, 'gust_mph': 8.6, 'gust_kph': 13.8, 'short_rad': 0, 'diff_rad': 0, 'dni': 0, 'gti': 0}}
