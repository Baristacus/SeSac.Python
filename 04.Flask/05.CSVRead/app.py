from flask import Flask
from flask import render_template
from flask import request
import csv

app = Flask(__name__)

csv_data = []
page = 1
total_page = 1


def load_csv(filename):
    with open(filename, newline="", encoding="UTF-8") as file:
        csv_reader = csv.reader(file)
        for data in csv_reader:
            csv_data.append(data)


def load_csv_dict(filename):
    with open(filename, newline="", encoding="UTF-8") as file:
        csv_reader = csv.DictReader(file)
        for data in csv_reader:
            csv_data.append(data)


@app.route("/")
def index():
    return render_template("index.html", users=csv_data)


@app.route("/<int:page>")
def page(page):
    header = csv_data[0]
    per_page = 10
    data = csv_data[10 * (page - 1) : per_page * page + 1]
    total_page = int(len(csv_data) / per_page)
    current_page = page
    return render_template(
        "index.html",
        header=header,
        users=data,
        total_page=total_page,
        current_page=current_page,
    )


if __name__ == "__main__":
    load_csv("./user.csv")
    # load_csv_dict("./data.csv")
    app.run(debug=True)
