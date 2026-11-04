
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
print("API key loaded:", bool(API_KEY))
print("API key length:", len(API_KEY) if API_KEY else 0)

BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_weather(city):

    if not API_KEY:
        print("Error: API key not found. Check your .env file.")
        return

    try:
        # Fetch current weather
        current_url = f"{BASE_URL}/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            current_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        current_data = response.json()

        # Display current weather
        print("\n========== CURRENT WEATHER ==========")

        print("City:", current_data["name"])
        print("Country:", current_data["sys"]["country"])

        print(
            "Temperature:",
            current_data["main"]["temp"], "°C"
        )

        print(
            "Humidity:",
            current_data["main"]["humidity"], "%"
        )

        print(
            "Description:",
            current_data["weather"][0]["description"].title()
        )

        print(
            "Feels Like:",
            current_data["main"]["feels_like"], "°C"
        )

        # Fetch 5-day forecast
        forecast_url = f"{BASE_URL}/forecast"

        forecast_response = requests.get(
            forecast_url,
            params=params,
            timeout=10
        )

        forecast_response.raise_for_status()

        forecast_data = forecast_response.json()

        # Group forecast by date
        daily_forecast = {}

        for item in forecast_data["list"]:

            date = item["dt_txt"].split(" ")[0]

            # Prefer forecast closest to 12 noon
            forecast_time = datetime.strptime(
                item["dt_txt"], "%Y-%m-%d %H:%M:%S"
            )

            distance = abs(forecast_time.hour - 12)

            if date not in daily_forecast:
                daily_forecast[date] = (distance, item)

            elif distance < daily_forecast[date][0]:
                daily_forecast[date] = (distance, item)

        # Display forecast
        print("\n========== 5-DAY FORECAST ==========")

        for date, (distance, item) in daily_forecast.items():

            day = datetime.strptime(
                date, "%Y-%m-%d"
            ).strftime("%A")

            temperature = item["main"]["temp"]
            description = item["weather"][0]["description"].title()
            humidity = item["main"]["humidity"]

            print("\nDate:", date)
            print("Day:", day)
            print("Temperature:", temperature, "°C")
            print("Description:", description)
            print("Humidity:", humidity, "%")

        print("\n====================================")
        print("Weather information fetched successfully!")

    except requests.exceptions.HTTPError as e:

        if e.response is not None and e.response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")

        elif e.response is not None and e.response.status_code == 401:
            print("Error: Invalid API key or API key not activated.")

        else:
            print("HTTP Error:", e)

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)

    except (KeyError, ValueError, IndexError) as e:
        print("Error: Unable to read weather data:", e)


def main():

    print("===================================")
    print("       WEATHER APPLICATION")
    print("===================================")

    if not API_KEY:
        print("API key is missing. Please check your .env file.")
        return

    city = input("\nEnter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
