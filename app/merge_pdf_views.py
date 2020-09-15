from flask import render_template, redirect, url_for

from app import app
from app.forms import MergeForm
from app.utils import verify_filenames, merge_pdfs


@app.route("/", methods=["GET", "POST"])
def index():
    form = MergeForm()
    if form.validate_on_submit():
        uploaded_files = [file["file"] for file in form.documents.data if file["file"]]
        secured_files = verify_filenames(uploaded_files)
        is_done = merge_pdfs(file_list=secured_files)
        if is_done:
            return redirect(url_for("output", mode="merged"))
    return render_template("index.html", form=form, page_title="merged")
