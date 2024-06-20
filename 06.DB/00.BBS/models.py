from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):  # 나의 객체를 누군가 print할때, 표현해주고 싶은 함수
        return f"<User {self.id}, {self.username}>"


class Bbs(db.Model):
    __tablename__ = "bbs"
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)


class BbsComment(db.Model):
    __tablename__ = "bbs_comment"
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    depth = db.Column(db.Integer, nullable=False)
    bbs_id = db.Column(db.ForeignKey("bbs.id"), nullable=False)
