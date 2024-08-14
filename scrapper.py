import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://gothamist.com/search?q=h1n1"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

posts = []
for row in soup.select("div.gothamist-card"):
    title = row.find("div", class_="h2").get_text()
    subtitle = row.find("div", class_="card-slot").find("p").get_text()
    authorName = row.find("a", class_="v-byline-author-name").get_text()
    posts.append([title, subtitle, authorName])

df = pd.DataFrame(posts, columns=["Title", "Subtitle", "Author Name"])
df.to_csv("news.csv", index=False)