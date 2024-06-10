from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/user/<username>")
def user(username):
    return f"Hello, {username}"


@app.route("/user/<int:age>")
def age(age):
    return f"Age: {age}"


@app.route("/user/<username>/<int:age>")
def user_age(username, age):
    return f"Hello, {username}! Age: {age}"


if __name__ == "__main__":
    app.run(debug=True)
