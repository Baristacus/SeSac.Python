import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("KAKAO_API_KEY")

url = "https://dapi.kakao.com/v2/search/image"

params = {"query": "파이썬", "size": 5}
headers = {"Authorization": f"KakaoAK {API_KEY}"}

response = requests.get(url, params=params, headers=headers)
response.raise_for_status()

data = response.json()
for item in data["documents"]:
    thumbnail_url = item["thumbnail_url"]
    image_url = item["image_url"]

    print(f"썸네일 URL: {thumbnail_url}")
    print(f"이미지 URL: {image_url}")
    print("=" * 100)
