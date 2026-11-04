# Weather App with Live API

## Project Description
A Python-based Weather Application that fetches real-time weather information using the OpenWeather API.

## Features
- Displays current temperature.
- Shows humidity and weather description.
- Displays feels-like temperature.
- Provides a 5-day weather forecast.
- Accepts different city names.
- Handles invalid cities and network errors.
- Uses an environment file to protect the API key.

## Technologies Used
- Python
- Requests
- OpenWeather API
- JSON
- Python-dotenv

## Installation

Install the required libraries:

```bash
pip install requests python-dotenv
```

## API Key Setup

1. Create an account at https://openweathermap.org/
2. Generate an API key.
3. Create a `.env` file in the project folder.
4. Add your API key:

```env
OPENWEATHER_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your own API key.

**Important:** Never upload your `.env` file to GitHub.

## How to Run

Open the terminal in the project folder and execute:

```bash
python weather_app.py
```

Enter a city name to view its current weather and forecast.

## Project Status
Completed successfully.