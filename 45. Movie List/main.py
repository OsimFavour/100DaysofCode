from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2"

response = requests.get(URL)
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")

movies = soup.find_all("h3", {"class": "title"})

movie_list = [movie.getText() for movie in movies]
movie_order = movie_list[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:   
    for movie in movie_order:
        file.write(f"{movie}\n")
        
