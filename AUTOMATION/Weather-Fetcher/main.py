import requests

API_KEY = "2bbeda463cc69a3f61f692d040f85837"
BASE_URL =  "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)