import requests


class JSONPlaceHolderAPI:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/"

    def get_posts_by_user_id(self, user_id):
        url = f"{self.base_url}posts?userId={user_id}"
        response = requests.get(url)
        return response.json()

    def get_comments_by_post_id(self, post_id):
        url = f"{self.base_url}posts/{post_id}/comments"
        response = requests.get(url)
        return response.json()

    def create_post(self, user_id, title, body):
        url = f"{self.base_url}posts"
        data = {"userId": user_id, "title": title, "body": body}
        response = requests.post(url, data=data)
        return response.json()
