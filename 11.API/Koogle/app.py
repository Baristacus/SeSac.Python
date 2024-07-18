from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("KAKAO_API_KEY")


def call_kakao_api(api_url, params):
    headers = {"Authorization": f"KakaoAK {API_KEY}"}
    response = requests.get(api_url, headers=headers, params=params)
    return response.json()


@app.route("/")
def index():
    return render_template("index.jinja2")


@app.route("/search")
def search():
    query = request.args.get("query")
    query_type = request.args.get("type")

    if query_type == "web":
        api_url = "https://dapi.kakao.com/v2/search/web"
    elif query_type == "image":
        api_url = "https://dapi.kakao.com/v2/search/image"
    elif query_type == "video":
        api_url = "https://dapi.kakao.com/v2/search/video"

    params = {"query": query, "type": query_type, "size": 10}

    result = call_kakao_api(api_url, params)
    return render_template(
        "results.jinja2", query=query, result=result["documents"], query_type=query_type
    )


if __name__ == "__main__":
    app.run(debug=True)
