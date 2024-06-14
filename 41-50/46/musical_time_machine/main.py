import requests
from bs4 import BeautifulSoup

date = input("What YYYY-MM-DD would you like the top 100 songs for? \n")

billboard_base_url = "https://billboard.com/charts/hot-100"

response = requests.get(url=f"{billboard_base_url}/{date}")
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

song_name_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_spans]

print(song_names)
