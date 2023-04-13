import os

from src.util import get_upload_file_path


def ensure_upload_path(app, _):
    upload_file_path = get_upload_file_path()
    if not os.path.exists(upload_file_path):
        os.mkdir(upload_file_path)
