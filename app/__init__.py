from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["UPLOAD_PATH"] = "uploads"
app.config["MERGED_FILES"] = "merged"
app.config["SPLIT_FILES"] = "split"
app.config["ALLOWED_EXTENSION"] = ".pdf"
app.config["MAX_CONTENT_LENGTH"] = 6 * 1024 * 1024
from app import merge_pdf_views
from app import split_pdf_views
from app import encrypt_pdf_views
