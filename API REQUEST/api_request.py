import requests
from dotenv import load_dotenv
import os

load_dotenv()
auth_api_weather = os.getenv("auth_api_weather")

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

# Complete API endpoint for current weather
base_url = 'http://api.weatherapi.com/v1/current.json'

# Example: Get current weather for London
data = get_api(base_url, auth_api_weather, "Jakarta")
print(data)