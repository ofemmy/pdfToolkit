import os

from flask import render_template

from app import app


@app.route("/result/<mode>", methods=["GET"])
def output(mode="merge"):
    files = os.listdir(app.config["MERGED_FILES"])
    if mode == "split":
        files = [file for file in os.listdir(app.config["SPLIT_FILES"]) if file.endswith(".zip")]
    return render_template("result.html", files=files, mode=mode)
