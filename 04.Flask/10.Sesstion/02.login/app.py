from flask import Flask, session, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:3000"}})

app.secret_key = "secret"

users = [
    {"name": "Alice", "id": "alice", "password": "alice1234"},
    {"name": "Bob", "id": "bob", "password": "bob1234"},
    {"name": "Charlie", "id": "charlie", "password": "charlie1234"},
    {"name": "David", "id": "david", "password": "david1234"},
]


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    id = data["id"]
    password = data["password"]

    user = next(
        (user for user in users if user["id"] == id and user["password"] == password),
        None,
    )

    if user:
        session["user"] = user
        return jsonify({"response": "success", "message": "로그인 성공"})

    else:
        return jsonify({"response": "fail", "message": "로그인 실패"})


@app.route("/api/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        user = session.get("user")
        return jsonify({"response": "success", "user": user})

    else:
        newpassword = request.form["newpassword"]

        for user in users:
            if user["id"] == session["user"]["id"]:
                user["password"] = newpassword
                session["user"] = user
                return (
                    jsonify({"response": "success", "message": "비밀번호 변경 성공"}),
                    200,
                )


@app.route("/api/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    return jsonify({"response": "success"})


if __name__ == "__main__":
    app.run(debug=True)
