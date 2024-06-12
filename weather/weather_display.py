# weather/weather_display.py
import logging

def display_weather(weather_data):
    if weather_data:
        city = weather_data.get('name')
        weather = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        logging.info(f"Displaying weather data for {city}")
        print(f"Weather in {city}:")
        print(f"  Condition: {weather.capitalize()}")
        print(f"  Temperature: {temp}°C (Feels like: {feels_like}°C)")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")
    else:
        logging.error("No weather data to display.")
        print("Could not fetch weather data.")
