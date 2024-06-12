from flask import Flask
from flask import render_template
from flask import request
import csv

app = Flask(__name__)

csv_data = []
page = 1
total_page = 1
headers = []


def load_csv(filename):
    with open(filename, newline="", encoding="UTF-8") as file:
        csv_reader = csv.reader(file)
        for data in csv_reader:
            csv_data.append(data)


def load_csv_dict(filename):
    global headers
    with open(filename, newline="", encoding="UTF-8") as file:
        csv_reader = csv.DictReader(file)
        headers = [h for h in csv_reader.fieldnames]
        for data in csv_reader:
            csv_data.append(data)


@app.route("/")
def index():
    return render_template("index.html", users=csv_data)


@app.route("/<int:page>")
def page(page):
    per_page = 10
    data = csv_data[10 * (page - 1) : per_page * page]
    total_page = int(len(csv_data) / per_page)
    current_page = page
    return render_template(
        "index.html",
        header=headers,
        users=data,
        total_page=total_page,
        current_page=current_page,
    )


@app.route("/user/<Id>")
def user(Id):
    u_detail = [user for user in csv_data if user["Id"] == Id]
    return render_template("user.html", header=headers, users=u_detail)


if __name__ == "__main__":
    # load_csv("./user.csv")
    load_csv_dict("./user.csv")
    app.run(debug=True)
