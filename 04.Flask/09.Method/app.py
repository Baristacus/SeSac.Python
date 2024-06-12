from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

users = [
    {"name": "Alice", "id": "alice", "password": "alice1234"},
    {"name": "Bob", "id": "bob", "password": "bob1234"},
    {"name": "Charlie", "id": "charlie", "password": "charlie1234"},
    {"name": "David", "id": "david", "password": "david1234"},
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    else:
        id = request.form["id"]
        password = request.form["password"]

        for user in users:
            if user["id"] == id and user["password"] == password:
                return render_template("index.html", user=user)
            else:
                return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
