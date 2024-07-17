from my_jsonplaceholder_api import JSONPlaceHolderAPI

api = JSONPlaceHolderAPI()
user_posts = api.get_posts_by_user_id(1)

for comment in user_posts:
    print(f"{comment['title']}")
