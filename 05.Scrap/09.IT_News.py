import requests
from bs4 import BeautifulSoup


url = "https://news.naver.com/section/105"

data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")


def headline():
    headlines = [
        li.select_one("strong").text
        for li in soup.find_all("li", class_="sa_item _SECTION_HEADLINE")
    ]
    headlines_link = [
        a["href"]
        for li in soup.find_all("li", class_="sa_item _SECTION_HEADLINE")
        for a in li.find_all("a", class_="sa_text_title")
    ]

    return list(zip(headlines, headlines_link))


def dailynews():
    newstitles = [
        li.select_one("strong").text
        for li in soup.find_all("li", class_="sa_item _LAZY_LOADING_WRAP")
    ]
    newslinks = [
        a["href"]
        for li in soup.find_all("li", class_="sa_item _LAZY_LOADING_WRAP")
        for a in li.find_all("a", class_="sa_text_title")
    ]

    return list(zip(newstitles, newslinks))


print(headline())
print(dailynews())
