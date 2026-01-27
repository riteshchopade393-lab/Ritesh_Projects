import requests

API_KEY = "b70e12b71333b1253f3b3e458fcf2b56"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": f"{city},IN",
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("❌ Error:", response.status_code)
        print(response.json())
        return

    data = response.json()

    print("\n🌍 Weather Report")
    print("-" * 25)
    print(f"City        : {data['name']}")
    print(f"Temperature : {data['main']['temp']}°C")
    print(f"Feels Like  : {data['main']['feels_like']}°C")
    print(f"Condition   : {data['weather'][0]['description'].title()}")
    print(f"Humidity    : {data['main']['humidity']}%")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")

city = input("Enter city name: ")
get_weather(city)
