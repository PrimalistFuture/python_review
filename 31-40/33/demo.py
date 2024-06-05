import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# If we don't get a 200, then an exception is raised
response.raise_for_status()
data = response.json()
position_data = data["iss_position"]
longitude_data = position_data["longitude"]
latitude_data = position_data["latitude"]
