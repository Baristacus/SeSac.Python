from flask import Blueprint, render_template

product = Blueprint("product", __name__)


@product.route("/")
def index():
    return render_template("product/index.html")


@product.route("/fruit")
def fruit():
    return "Fruit Page"


@product.route("/vegetable")
def vegetable():
    return "Vegetable Page"
