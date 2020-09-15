from flask import render_template

from app import app
from app.forms import MergeForm


@app.route("/")
def index():
    form = MergeForm()
    return render_template("index.html", form=form)
