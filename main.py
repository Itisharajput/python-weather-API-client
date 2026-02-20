import requests
from config import API_KEY, BASE_URL


def get_weather(city):
    """Fetch weather data from API."""
    if not API_KEY:
        print("API key is not configured.")
        return None

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error fetching data from API.")
        return None


def display_weather(data):
    """Display formatted weather data."""
    if data:
        print("City:", data.get("name"))
        print("Temperature:", data["main"]["temp"], "°C")
        print("Condition:", data["weather"][0]["description"])
    else:
        print("No data available.")


def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
