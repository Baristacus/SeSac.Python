from bs4 import BeautifulSoup
import requests


url = "https://sports.news.naver.com/index"

data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")

# 신문 기사제목 및 링크 출력하기

titles = soup.select("ul.today_list li")
today_titles = []
today_news = []

for title in titles:
    a_tag = title.select_one("a")["title"]
    a_href = title.select_one("a")["href"]
    today_titles.append(a_tag)
    today_news.append(a_href)

print(today_titles)
print(today_news)

# print(titles[2])
