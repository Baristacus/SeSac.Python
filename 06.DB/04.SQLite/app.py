from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta
import database as db

app = Flask(__name__)
app.secret_key = "hello1234"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        # 사용자 데이터를 저장
        db.execute_query(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email),
        )
        flash("회원가입이 완료되었습니다.")
        return redirect(url_for("login"))
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # 로그인 처리 구현
        username = request.form["username"]
        password = request.form["password"]

        # 사용자 데이터를 외부 DB에서 가져오기
        # query = "SELECT * FROM users WHERE username = ? AND password = ?"
        user_data = db.get_query(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        print(f"조회된 사용자: ", user_data)

        if len(user_data) == 1:  # and user_data["password"] == password
            session["user"] = username
            session.permanent = True
            print("패스워드 맞음!!")
            flash("로그인에 성공하였습니다.")
            return redirect(url_for("home"))
        else:
            print("패스워드 틀림!!")
            flash("아이디/패스워드가 일치하지 않습니다.")
            # 메세지가 있으면 전달하고, 없으면 그냥 재 로그인
            return redirect(url_for("login"))
    else:
        # GET 요청이라서 로그인 폼 보여주기
        if "user" in session:
            print("이전에 로그인 했음!!")
            return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/user", methods=["GET", "POST"])
def user():
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            if email == "" and password != "":
                db.execute_query(
                    "UPDATE users SET password = ? WHERE username = ?", (password, user)
                )
                flash("패스워드가 변경되었습니다.")
            else:
                db.execute_query(
                    "UPDATE users SET email = ? WHERE username = ?", (email, user)
                )
                flash("이메일이 변경되었습니다.")
            return redirect(url_for("user"))

        return render_template("user.html")


@app.route("/view")
def view():
    users = db.get_query("SELECT * FROM users", ())
    return render_template("view.html", users=users)


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("로그아웃에 성공하였습니다.")
    return redirect(url_for("login"))


@app.route("/delete/user")
def delete():
    db.execute_query("DELETE FROM users WHERE username = ?", (session["user"],))
    flash("계정이 삭제되었습니다.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.init_db()  # 시스템 부팅(?) 시에 DB 초기화 하기...
    print("DB 초기화 완료")
    app.run(debug=True)  # 플라스크 앱 실행...
