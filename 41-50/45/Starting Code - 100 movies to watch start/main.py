import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movie_titles.reverse()

with open("41-50/45/Starting Code - 100 movies to watch start/movies.txt", "a", encoding="UTF-8") as file:
    for title in movie_titles:
        title = title.replace(")", ".")
        file.write(f"{title}\n")
