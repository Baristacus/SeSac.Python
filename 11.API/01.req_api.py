import requests

url = "https://jsonplaceholder.typicode.com/"

# user_id = 1
# response1 = requests.get(url + "posts" + "?userId=" + str(user_id))

# print(f"{response1.text}")


post_id = 1
response2 = requests.get(url + "posts/" + str(post_id) + "/comments")

print(f"{response2.text}")
