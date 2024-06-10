from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/user")
@app.route("/user/<username>")
def user(username=None):
    friends = ["alice", "bob", "charlie"]
    return render_template("user.html", username=username, friends=friends)


if __name__ == "__main__":
    app.run(debug=True)
