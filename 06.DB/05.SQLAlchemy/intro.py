from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

user = User(name="alice", age=20)
session.add(user)
session.commit()

user2 = User(name="bob", age=30)
session.add(user2)
session.commit()

users = session.query(User).all()

for user in users:
    print(user.name, user.age)
