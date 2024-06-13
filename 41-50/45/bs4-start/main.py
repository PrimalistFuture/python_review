from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a")
    article_links.append(link)

# print(article_links, article_texts)

article_scores = [int(score.getText().split(" ")[0])
                  for score in soup.find_all(name="span", class_="score")]
max_score = max(article_scores)
max_idx = article_scores.index(max_score)


highest_rated_article = [
    article_texts[max_idx],
    article_links[max_idx],
    article_scores[max_idx]
]
print(highest_rated_article)
