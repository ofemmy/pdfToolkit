from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, FieldList, FormField, Form


class FileForm(Form):
    file = FileField("file", validators=[FileAllowed(upload_set=["pdf"], message="Only pdfs are allowed")])


class MergeForm(FlaskForm):
    documents = FieldList(FormField(FileForm), min_entries=4)


class SplitForm(FlaskForm):
    pdf = FileField("file", validators=[FileRequired(message="Field cannot be empty"),
                                        FileAllowed(upload_set=["pdf"], message="Only pdfs are allowed")])
