from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

users = [
    {"name": "Alice", "age": "37", "location": "Seoul", "car": "BMW"},
    {"name": "Alice", "age": "25", "location": "Seoul", "car": "BMW"},
    {"name": "Alice.Jr", "age": "2", "location": "Busan", "car": ""},
    {"name": "Bob", "age": "37", "location": "Busan", "car": "Mercedes"},
    {"name": "Bob", "age": "27", "location": "Busan", "car": "Mercedes"},
    {"name": "Bob.Jr", "age": "5", "location": "Busan", "car": ""},
    {"name": "Bob.Jr", "age": "7", "location": "Busan", "car": ""},
    {"name": "Charlie", "age": "35", "location": "Daegu", "car": "Audi"},
    {"name": "Charlie", "age": "40", "location": "Daegu", "car": "Audi"},
    {"name": "Charlie.Jr", "age": "10", "location": "Daegu", "car": ""},
    {"name": "Charlie.Jr", "age": "4", "location": "Daegu", "car": ""},
]


@app.route("/")
def index():
    return render_template("index.html", users=users)


@app.route("/search")
def search():
    name_query = request.args.get("name")
    age_query = request.args.get("age")

    result = []

    if name_query:
        for user in users:
            if user["name"].lower() == name_query.lower():
                result.append(user)

    if age_query:
        for user in result:
            if int(user["age"]) == int(age_query):
                result.append(user)

    return render_template("index.html", users=result)


if __name__ == "__main__":
    app.run(debug=True)
