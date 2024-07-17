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
    api_url = "https://dapi.kakao.com/v2/search/web"
    params = {"query": query, "size": 10}

    result = call_kakao_api(api_url, params)
    return render_template("results.jinja2", query=query, result=result["documents"])


if __name__ == "__main__":
    app.run(debug=True)
