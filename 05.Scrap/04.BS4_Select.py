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
        <p>Copyright C <b>2024.</b> <i>이 페이지는</i> 내거</p>
    </div>
</body>
</html>"""

# html_doc = requests.get('https://www.naver.com').text

soup = BeautifulSoup(html_doc, "html.parser")  # DOM으로 파싱

link_tag = soup.select_one("a")
print(link_tag)

all_imgs = soup.select("img")
for img in all_imgs:
    print(img["src"])

content_div = soup.select_one("div.content")  # div 아래에 있는 .content <--클래스명
footer_div = soup.select_one("div#footer")
li_lists = soup.select(
    "div.content li"
)  # div 아래에 있는 content클래스 아래에 있는 li들

p_tag_div_footer = soup.select_one("div#footer p")
b_text = p_tag_div_footer.select_one("b").text
i_text = p_tag_div_footer.select_one("i").text

print(f"볼드텍스트: {b_text} 이탤릭텍스트: {i_text}")
