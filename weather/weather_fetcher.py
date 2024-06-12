# weather/weather_fetcher.py
import requests
import logging
from config import API_KEY, BASE_URL

def fetch_weather(city):
    logging.info(f"Fetching weather data for city: {city}")
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info("Weather data fetched successfully.")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return None
