import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Weather:", data["weather"][0]["description"])
            print("Humidity:", data["main"]["humidity"], "%")
        else:
            print("Error:", data.get("message", "Unable to get weather"))

    except requests.exceptions.RequestException:
        print("Internet connection error!")

city = input("Enter city name: ")
get_weather(city)
