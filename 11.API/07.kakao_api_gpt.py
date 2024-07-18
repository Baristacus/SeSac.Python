# coding=utf8
# REST API 호출에 필요한 라이브러리
import requests
import json
import os
from dotenv import load_dotenv

# .env 파일로부터 환경변수 로드
load_dotenv()

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
API_KEY = os.environ.get("KAKAO_API_KEY")
REST_API_KEY = API_KEY


# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens=1, temperature=1.0, top_p=1.0, n=1):
    r = requests.post(
        "https://api.kakaobrain.com/v1/inference/kogpt/generation",
        json={
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "n": n,
        },
        headers={
            "Authorization": "KakaoAK " + REST_API_KEY,
            "Content-Type": "application/json",
        },
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response


# KoGPT에게 전달할 명령어 구성
prompt = """너 바보지"""

# 파라미터를 전달해 kogpt_api()메서드 호출
response = kogpt_api(prompt=prompt, max_tokens=32, temperature=1.0, top_p=1.0, n=3)

print(response["generations"][0]["text"])
