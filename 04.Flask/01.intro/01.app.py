from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/user/<username>")
def user(username):
    return "Hello, {}!".format(username)


if __name__ == "__main__":
    app.run(debug=True)
