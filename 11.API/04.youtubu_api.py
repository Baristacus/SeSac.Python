import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
search_query = "파이썬 플라스크"

url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet",
    "q": search_query,
    "type": "video",
    "maxResults": 5,
    "key": API_KEY,
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

for item in data["items"]:
    video_title = item["snippet"]["title"]
    description = item["snippet"]["description"]

    print(f"제목: {video_title}")
    print(f"설명: {description}")
    print("=" * 100)
