import requests
from bs4 import BeautifulSoup

EMPIRE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(EMPIRE_URL)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

titles = soup.findAll(name="h3", class_="title")

ordered_movies = [title.getText() for title in reversed(titles)]

with open("./movies.txt", "w") as file:
    for movie in ordered_movies:
        file.write(f"{movie}\n")