import requests
from bs4 import BeautifulSoup
import random

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

soup = BeautifulSoup(response.text,'html.parser')

titles = soup.select(selector=".article-title-description__text > .title")
print(titles)
# for title in titles[::-1]:
#     with open('Movies.txt',mode='a',encoding="utf8") as file:
#         file.write(title.text+'\n')
    
    
# with open("Movies.txt") as file:
#     movies = file.readlines()
    
# movie = random.choice(movies)
# print(f"Today You can watch: {movie.split(")")[1]}")
    
    
    
