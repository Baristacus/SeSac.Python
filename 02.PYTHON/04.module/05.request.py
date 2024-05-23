import requests


# 웹 페이지에 있는 컨텐츠 가져오기
response1 = requests.get("https://example.com")
response2 = requests.get("https://jsonplaceholder.typicode.com/users")
# print(response)
# print(response.status_code)
# print(response.text)

data = response2.json()
for user in data:
    print(f"이름: {user["name"]} \n이메일: {user["email"]}")
