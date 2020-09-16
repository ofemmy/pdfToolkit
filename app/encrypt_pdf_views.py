from flask import render_template

from app import app


@app.route("/encrypt")
def encrypt():
    return render_template("index.html")
