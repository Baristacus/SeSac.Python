import requests
from bs4 import BeautifulSoup

# 직접 창에서 검색하지 않고 파싱으로 검색하는 방법

base_url = "https://www.google.co.kr/search"


def google_search(query):
    params = {"q": query}

    response = requests.get(base_url, params=params)
    return response.text


query = "파이썬 프로그래밍"
soup = google_search(query)

print(soup)
