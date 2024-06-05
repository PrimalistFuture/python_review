import requests
import datetime
API_KEY = "https://api.sunrise-sunset.org/json"

params = {  # these are the params the sunrise-sunset api wants
    "lat": 37.774929,
    "lng": -122.419418,
    "tzid": "America/Los_Angeles",
    "formatted": 0  # gives time in 24h
}
# this is how requests wants parameters
response = requests.get(url=API_KEY, params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_time = sunrise.split("T")[1].split(":")[0]  # drilling to just the hour
print(sunrise_time)

time_now = datetime.datetime.now()
