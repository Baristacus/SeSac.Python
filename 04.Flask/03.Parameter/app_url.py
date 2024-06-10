from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Alice.Jr", "age": 2, "location": "Busan", "car": ""},
    {"name": "Bob", "age": 37, "location": "Busan", "car": "Mercedes"},
    {"name": "Bob.Jr", "age": 5, "location": "Busan", "car": ""},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Charlie.Jr", "age": 10, "location": "Daegu", "car": ""},
]


@app.route("/")
def index():
    return jsonify(users)


@app.route("/user/<username>")
def user(username):
    for user in users:
        if user["name"].lower() == username.lower():
            return jsonify(user)
        if str(user["age"]) == username:
            return jsonify(user)
    return "User not found", 404


if __name__ == "__main__":
    app.run(debug=True)
