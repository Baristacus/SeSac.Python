from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from datetime import timedelta, datetime
from models import db, User, Bbs
from nanoid import generate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "sesac040620"
# app.permanent_session_lifetime = timedelta(minutes=60)

db.init_app(app)
bcrypt = Bcrypt(app)


@app.route("/", methods=["GET", "POST"])
def index():
    userList = User.query.all()
    bbsList = Bbs.query.order_by(Bbs.created_at.desc()).limit(5).all()
    if request.method == "GET":
        if "user" in session:
            username = session["user"]
            return render_template(
                "index.html", username=username, userList=userList, bbsList=bbsList
            )
        else:
            return render_template("index.html", bbsList=bbsList, userList=userList)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form["inputUsername"]
        password = request.form["inputPassword"]
        password2 = request.form["inputPassword2"]

        if password != password2:
            flash("비밀번호가 일치하지 않습니다.", "warning")
            return redirect(url_for("signup"))

        hashed_pw = bcrypt.generate_password_hash(password2).decode("utf-8")

        new_user = User(
            id=generate(),
            username=username,
            password=hashed_pw,
            created_at=datetime.now(),
        )
        db.session.add(new_user)
        db.session.commit()
        flash("새싹 회원 등록에 성공하였습니다.", "info")
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["inputUsername"]
        password = request.form["inputPassword"]

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session["user"] = username
            flash("로그인에 성공하였습니다.", "success")
            print(username)
            return redirect(url_for("bbsList", username=username))
        else:
            flash("일치하는 회원정보가 없습니다.", "info")
            return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("정상적으로 로그아웃 되었습니다.", "success")
    return redirect(url_for("index"))


@app.route("/mypage")
def mypage():
    if "user" in session:
        username = session["user"]
        user = User.query.filter_by(username=username).first()
        mybbsList = Bbs.query.filter_by(username=username).all()
        return render_template(
            "mypage.html", username=username, user=user, mybbsList=mybbsList
        )
    else:
        flash(
            "새싹 회원이 아닌경우 접근할 수 없습니다. 로그인 또는 회원가입을 해주세요.",
            "danger",
        )
        return redirect(url_for("login"))


@app.route("/bbs/list", methods=["GET"])
def bbsList():
    if request.method == "GET":
        if "user" in session:
            username = session["user"]
            bbsList = Bbs.query.all()
            return render_template("bbs_list.html", username=username, bbsList=bbsList)
        else:
            flash(
                "새싹 회원이 아닌경우 접근할 수 없습니다. 로그인 또는 회원가입을 해주세요.",
                "danger",
            )
            return redirect(url_for("login"))


@app.route("/bbs/write", methods=["GET", "POST"])
def bbsWrite():
    if request.method == "GET":
        if "user" in session:
            username = session["user"]
            return render_template("bbs_write.html", username=username)
        else:
            flash(
                "새싹 회원이 아닌경우 접근할 수 없습니다. 로그인 또는 회원가입을 해주세요.",
                "danger",
            )
            return redirect(url_for("login"))

    if request.method == "POST":
        username = session["user"]
        title = request.form["inputTitle"]
        content = request.form["inputContent"]

        current_user = User.query.filter_by(username=username).first()

        new_bbs = Bbs(
            id=generate(),
            username=username,
            title=title,
            content=content,
            created_at=datetime.now(),
            user_id=current_user.id,
        )
        db.session.add(new_bbs)
        db.session.commit()
        flash("새로운 글이 등록되었습니다.", "success")
        return redirect(url_for("bbsList", username=username))


@app.route("/bbs/view/<id>", methods=["GET", "POST"])
def bbsView(id):
    if request.method == "GET":
        if "user" in session:
            username = session["user"]
            bbs = Bbs.query.filter_by(id=id).first()
            return render_template("bbs_view.html", username=username, bbs=bbs)
        else:
            flash(
                "새싹 회원이 아닌경우 접근할 수 없습니다. 로그인 또는 회원가입을 해주세요.",
                "danger",
            )
            return redirect(url_for("login"))


@app.route("/bbs/update/<id>", methods=["GET", "POST"])
def bbsUpdate(id):
    if request.method == "GET":
        if "user" in session:
            username = session["user"]
            bbs = Bbs.query.filter_by(id=id).first()
            if bbs.username == session["user"]:
                return render_template("bbs_update.html", username=username, bbs=bbs)
            else:
                flash("본인이 쓴 글이 아닌경우 접근할 수 없습니다.", "danger")
                return redirect(url_for("bbsList", username=username))
        else:
            flash(
                "새싹 회원이 아닌경우 접근할 수 없습니다. 로그인 또는 회원가입을 해주세요.",
                "danger",
            )
            return redirect(url_for("login"))

    if request.method == "POST":
        username = session["user"]
        title = request.form["inputTitle"]
        content = request.form["inputContent"]

        bbs = Bbs.query.filter_by(id=id).first()
        bbs.title = title
        bbs.content = content
        bbs.updated_at = datetime.now()

        db.session.commit()
        flash("새로운 글이 수정되었습니다.", "success")
        return redirect(url_for("bbsView", id=id, username=username))


@app.route("/bbs/delete/<id>")
def bbsDelete(id):
    if "user" in session:
        username = session["user"]
        bbs = Bbs.query.filter_by(id=id).first()
        db.session.delete(bbs)
        db.session.commit()
        flash("글이 삭제되었습니다.", "success")
        return redirect(url_for("bbsList", username=username))
    else:
        flash(
            "새싹 회원이 아닌경우 접근할 수 없습니다. 로그인 또는 회원가입을 해주세요.",
            "danger",
        )
        return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():  # Flask 앱이 추기화가 끝난 상태에서 db 초기화 실행
        db.create_all()
    app.run(debug=True)
