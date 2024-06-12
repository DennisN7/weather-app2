# main.py
import logging
from weather.weather_fetcher import fetch_weather
from weather.weather_display import display_weather

# Set up logging
logging.basicConfig(filename='weather_app.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def main():
    logging.info("Weather Application started.")
    city = input("Enter the city name: ")
    logging.info(f"City entered: {city}")
    
    weather_data = fetch_weather(city)
    display_weather(weather_data)
    
    logging.info("Weather Application finished.")

if __name__ == "__main__":
    main()
