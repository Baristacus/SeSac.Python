from flask import Flask, session

app = Flask(__name__)

app.secret_key = "secret"


@app.route("/")
def index():
    session["username"] = "user1234"
    session["data"] = "1234"
    return "Hello World!"


@app.route("/set_session")
def set_session(id):

    session["username"] = id

    return f"데이터 저장완료"


@app.route("/get_session")
def get_session():

    username = session.get("username")
    data = session.get("data")

    return username, data


# 쿠키저장
# curl 127.0.0.1:5000 -c cookie.txt
# 쿠키들고가기
# curl 127.0.0.1:5000 -b cookie.txt

if __name__ == "__main__":
    app.run(debug=True)
