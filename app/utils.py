import os
import shutil

from PyPDF2 import PdfFileReader, PdfFileWriter
from flask import current_app
from werkzeug.utils import secure_filename


def verify_filenames(pdf_files):
    for idx, file in enumerate(pdf_files):
        filename = secure_filename(file.filename)
        if filename == "":
            file.filename = "Uploaded-file-" + str(idx)
    return pdf_files


def merge_pdfs(file_list):
    pdf_writer = PdfFileWriter()
    for file in file_list:
        pdf = PdfFileReader(file)
        for page in range(pdf.getNumPages()):
            pdf_writer.addPage(pdf.getPage(page))
    try:
        with open(os.path.join(current_app.config["MERGED_FILES"], "merged.pdf"), "wb") as out:
            pdf_writer.write(out)
        return True
    except Exception as e:
        print(e)
        return False


def split_pdf(pdf_file):
    pdf = PdfFileReader(pdf_file)
    try:
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            split_pdf_name = f"{pdf_file.filename.split('.')[0]}-{page}.pdf"
            with open(os.path.join(current_app.config["UPLOAD_PATH"], split_pdf_name), 'wb') as output_file:
                pdf_writer.write(output_file)
        return zip_files()
    except Exception as e:
        print(e)
        return False


def zip_files():
    split_files_dir = current_app.config["UPLOAD_PATH"]
    out_dir = current_app.config["SPLIT_FILES"]
    destination = os.path.join(out_dir, "output")
    try:
        shutil.make_archive(base_name=destination, format="zip", root_dir=split_files_dir)
        return True
    except Exception as e:
        print(e)
        raise e


def clean_up_uploads():
    upload_dir=current_app.config["UPLOAD_PATH"]
    files = os.listdir(upload_dir)
    for f in [file for file in files if file.endswith(".pdf")]:
        f_path = os.path.join(upload_dir, f)
        os.remove(f_path)
