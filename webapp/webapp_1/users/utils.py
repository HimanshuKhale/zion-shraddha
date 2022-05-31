import os
import secrets
from PIL import Image
from flask import url_for
from flask import current_app

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def save_pdf(form_pdf):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_pdf.filename)
    pdf_fn = random_hex + f_ext
    pdf_path = os.path.join(current_app.root_path, 'static/pdf_file', pdf_fn)

    return pdf_fn

