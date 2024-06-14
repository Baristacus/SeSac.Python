import requests
from bs4 import BeautifulSoup

baseUrl = "https://search.naver.com/search.naver"


def naver_search(query):
    params = {"query": query}
    response = requests.get(baseUrl, params=params)

    return response.text


kw = input("검색어를 입력하세요: ")
print(naver_search(kw))
