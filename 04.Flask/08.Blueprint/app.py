from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint

from admin.admin import admin
from product.product import product
from user.user import user

app = Flask(__name__)

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(product, url_prefix="/product")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
