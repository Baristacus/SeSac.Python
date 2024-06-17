from bs4 import BeautifulSoup
import requests


url = "https://www.pythonscraping.com/pages/page3.html"

data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")

# 상품명과 가격 출력
item_table = soup.select_one("table#giftList")
items = []
prices = []
tds = item_table.select("td")

for i in range(1, 6):
    item = item_table.select_one(f"tr#gift{i}").td.text.strip()
    price = item_table.select(f"tr#gift{i} td")[2].text.strip()
    items.append(item)
    prices.append(price)

print(list(zip(items, prices)))


"""item1 = item_table.select_one('tr#gift1').td.text.strip()
item2 = item_table.select_one('tr#gift2').td.text.strip()
item3 = item_table.select_one('tr#gift3').td.text.strip()
item4 = item_table.select_one('tr#gift4').td.text.strip()
item5 = item_table.select_one('tr#gift5').td.text.strip()
items = [item1,item2,item3,item4,item5]
price1 = item_table.select('tr#gift1 td')[2].text.strip()
price2 = item_table.select('tr#gift2 td')[2].text.strip()
price3 = item_table.select('tr#gift3 td')[2].text.strip()
price4 = item_table.select('tr#gift4 td')[2].text.strip()
price5 = item_table.select('tr#gift5 td')[2].text.strip()
prices = [price1,price2,price3,price4,price5]
"""
