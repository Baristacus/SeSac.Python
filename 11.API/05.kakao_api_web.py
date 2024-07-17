import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("KAKAO_API_KEY")

url = "https://dapi.kakao.com/v2/search/web"
params = {"query": "파이썬", "size": 5}
headers = {"Authorization": f"KakaoAK {API_KEY}"}

response = requests.get(url, params=params, headers=headers)
response.raise_for_status()

data = response.json()
for item in data["documents"]:
    title = item["title"].replace("<b>", "").replace("</b>", "")
    url = item["url"]

    print(f"제목: {title}")
    print(f"URL: {url}")
    print("=" * 100)
