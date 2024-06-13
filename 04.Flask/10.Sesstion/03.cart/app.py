from flask import Flask
from flask import render_template, redirect, url_for
from flask import session
from datetime import timedelta


app = Flask(__name__)

app.secret_key = "secret"
app.permanent_session_lifetime = timedelta(minutes=5)

items = {
    "item1": {"name": "상품1", "price": 3000, "image": "image1.jpg"},
    "item2": {"name": "상품2", "price": 4000, "image": "image2.jpg"},
    "item3": {"name": "상품3", "price": 4000, "image": "image3.jpg"},
}


@app.route("/")
def index():
    return render_template("index.html", items=items)


@app.route("/add-cart/<item_name>")
def add_cart(item_name):

    if "cart" not in session:
        session["cart"] = {}
        session.permanent = True

    if item_name in session["cart"]:
        session["cart"][item_name] += 1
    else:
        item_info = items.get(item_name)
        if item_info:
            session["cart"][item_name] = 1

    session.modified = True

    return redirect(url_for("index"))


@app.route("/cart")
def cart():
    cart_items = {}
    total_price = 0

    if "cart" not in session:
        return redirect(url_for("index"))

    for item_name, quantity in session["cart"].items():
        item = items.get(item_name)
        if item:
            cart_items[item_name] = {
                "name": item["name"],
                "price": format(item["price"], ",d"),
                "quantity": quantity,
                "image": item["image"],
            }
            total_price += item["price"] * quantity

    return render_template(
        "cart.html", cart_items=cart_items, total_price=format(total_price, ",d")
    )


@app.route("/clear-cart")
def clear_cart():
    session.clear()
    return redirect(url_for("index"))


@app.route("/remove-from-cart/<item_name>")
def remove_from_cart(item_name):
    if "cart" in session:
        if item_name in session["cart"]:
            session["cart"].pop(item_name)
            session.modified = True
    return redirect(url_for("cart"))


if __name__ == "__main__":
    app.run(debug=True)
