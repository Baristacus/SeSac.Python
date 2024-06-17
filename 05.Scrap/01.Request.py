import requests

url = "https://hiphople.com/fboard"

response = requests.get(url)

print(response.status_code)
print(response.text)
