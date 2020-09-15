from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
from app import merge_pdf_views
from app import split_pdf_views
