import requests
from dotenv import load_dotenv
import os

load_dotenv()
auth_api_weather = os.getenv("auth_api_weather")

# Complete API endpoint for current weather
<<<<<<< HEAD
base_url = 'http://api.weatherapi.com/v1/current.json'
=======
base_url_current = 'http://api.weatherapi.com/v1/current.json'
>>>>>>> 5a74b4af78ccf9db13717d022b35fd4f66136cf1

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
<<<<<<< HEAD
    return {'location': {'name': 'Jakarta', 'region': 'Jakarta Raya', 'country': 'Indonesia', 'lat': -6.2146, 'lon': 106.8451, 'tz_id': 'Asia/Jakarta', 'localtime_epoch': 1764678124, 'localtime': '2025-12-02 19:22'}, 'current': {'last_updated_epoch': 1764677700, 'last_updated': '2025-12-02 19:15', 'temp_c': 26.1, 'temp_f': 79.0, 'is_day': 0, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 5.6, 'wind_kph': 9.0, 'wind_degree': 356, 'wind_dir': 'N', 'pressure_mb': 1010.0, 'pressure_in': 29.83, 'precip_mm': 1.56, 'precip_in': 0.06, 'humidity': 84, 'cloud': 25, 'feelslike_c': 27.7, 'feelslike_f': 81.9, 'windchill_c': 29.2, 'windchill_f': 84.5, 'heatindex_c': 32.7, 'heatindex_f': 90.9, 'dewpoint_c': 22.5, 'dewpoint_f': 72.5, 'vis_km': 6.0, 'vis_miles': 3.0, 'uv': 0.0, 'gust_mph': 8.6, 'gust_kph': 13.8, 'short_rad': 0, 'diff_rad': 0, 'dni': 0, 'gti': 0}}
=======
    return {'location': {'name': 'Jakarta', 'region': 'Jakarta Raya', 'country': 'Indonesia', 'lat': -6.2146, 'lon': 106.8451, 'tz_id': 'Asia/Jakarta', 'localtime_epoch': 1764646901, 'localtime': '2025-12-02 10:41'}, 'current': {'last_updated_epoch': 1764646200, 'last_updated': '2025-12-02 10:30', 'temp_c': 31.3, 'temp_f': 88.3, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 2.2, 'wind_kph': 3.6, 'wind_degree': 227, 'wind_dir': 'SW', 'pressure_mb': 1011.0, 'pressure_in': 29.85, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 71, 'cloud': 50, 'feelslike_c': 38.5, 'feelslike_f': 101.2, 'windchill_c': 28.2, 'windchill_f': 82.7, 'heatindex_c': 31.4, 'heatindex_f': 88.5, 'dewpoint_c': 22.5, 'dewpoint_f': 72.4, 'vis_km': 7.0, 'vis_miles': 4.0, 'uv': 8.9, 'gust_mph': 6.7, 'gust_kph': 10.8, 'short_rad': 394.36, 'diff_rad': 103.25, 'dni': 0.0, 'gti': 103.18}}


>>>>>>> 5a74b4af78ccf9db13717d022b35fd4f66136cf1
