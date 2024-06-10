from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Alice", "age": 30, "location": "Busan", "car": "Audi"},
    {"name": "Alice.Jr", "age": 2, "location": "Busan", "car": ""},
    {"name": "Bob", "age": 37, "location": "Busan", "car": "Mercedes"},
    {"name": "Bob", "age": 40, "location": "Seoul", "car": "BMW"},
    {"name": "Bob.Jr", "age": 5, "location": "Busan", "car": ""},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Charlie.Jr", "age": 10, "location": "Daegu", "car": ""},
]


@app.route("/")
def index():
    return "Hello"


@app.route("/search")
def search():
    name_query = request.args.get("name")
    age_query = request.args.get("age")
    location_query = request.args.get("location")
    page = int(request.args.get("page", 1))

    result = []
    for user in users:
        if user["name"] == name_query:
            result.append(user)
        if int(user["age"]) == age_query:
            result.append(user)
        if user["location"] == location_query:
            result.append(user)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
