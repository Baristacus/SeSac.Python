from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title> 간단한 HTML 예제 </title>
</head>
<body>
    <h1>안녕하세요</h1>
    <p>이건 간단한 HTML 예제입니다.</p>
</body>
</html>"""

soup = BeautifulSoup(html_doc, "html.parser")  # html_parser, lxml
print(soup.head.title.text)
