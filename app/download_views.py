import os

from flask import send_from_directory

from app import app


@app.route("/download/<filename>")
def download(filename):
    file_dir = app.config["SPLIT_FILE"] if filename.endswith(".zip") else app.config["MERGED_FILES"]
    file_path_abs = os.path.abspath(file_dir)
    return send_from_directory(file_path_abs, filename, as_attachment=True)
