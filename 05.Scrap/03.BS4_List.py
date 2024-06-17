from bs4 import BeautifulSoup
import requests

html_doc = """
<html>
<head>
    <title> 간단한 HTML 예제 </title>
</head>
<body>
    <div class= "container">
        <h1>안녕하세요</h1>
        <p>이건 간단한 HTML 예제입니다.</p>
    </div>
    <a href="https://www.naver.com">네이버 링크</a>
    <img src="example.jpg" alt = "예제 이미지">
    <img src="example2.jpg" alt = "예제 이미지2" width="500" height="500">

    <div class= "content">
        <ul>
            <li> 항목1 </li>
            <li> 항목2 </li>
            <li> 항목3 </li>
        </ul>
    </div>
    <div id="footer">
        <p>Copyright C 2024. 이 페이지는 내거</p>
    </div>
</body>
</html>"""


soup = BeautifulSoup(html_doc, "html.parser")  # DOM으로 파싱

# list_items = soup.ul.find_all('li') # [<li> 항목1 </li>, <li> 항목2 </li>, <li> 항목3 </li>]
# print(list_items)

# for li in list_items:
#     print(li.text)

# '''
# #class가 container인 항목 가져오기
# container_div = soup.find('div',class_ = 'container')
# print(container_div.p.text)
# '''

# #footer를 가져다가 footer안의 글자 출력
# footer_id = soup.find('div',id = 'footer')
# print(footer_id.p.text)


# content_ul = soup.find('div',class_='content').ul

# for li in content_ul.find_all('li'):
#     print(li.text)

link_tag = soup.a  # 가장 먼저 DOM에서 잡히는 a태그
naver_link = link_tag["href"]

"""
response = requests.get(naver_link)
print(response.text)"""

img_tag = soup.img
print(img_tag["src"])
print(img_tag["alt"])

img_tags = soup.find_all("img")  # find 시리즈는 태그명 등으로 검색함.
img_tag1 = img_tags[0]
img_tag2 = img_tags[1]

# get은 키가 없으면 None을 찍어줌
print(f"소스: {img_tag1['src']}, ALT 글자: {img_tag1['alt']}")
print(
    f"소스: {img_tag2['src']}, ALT 글자: {img_tag2['alt']}, width: {img_tag2['width']}"
)
