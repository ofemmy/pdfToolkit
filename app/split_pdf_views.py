from flask import render_template
from werkzeug.utils import secure_filename

from app import app
from app.forms import SplitForm
from app.utils import split_pdf, clean_up_uploads


@app.route("/split", methods=["GET", "POST"])
def split():
    form = SplitForm()
    if form.validate_on_submit():
        uploaded_file = form.pdf.data
        uploaded_file.name = uploaded_file.name if secure_filename(uploaded_file.filename) else "uploaded_file"
        is_done = split_pdf(uploaded_file)
        if is_done:
            clean_up_uploads()
            print("done")
            # return redirect(url_for("output", mode="split"))
    return render_template("split.html", form=form, page_title="split")
