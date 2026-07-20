import requests

API_KEY = "2bbeda463cc69a3f61f692d040f85837"
BASE_URL =  "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)

    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} celsius")
else:
    print("An error occurred.")