import os
from pyngrok import ngrok


upload_file_path = "../upload/"


def ensure_upload_path(app, _):
    if not os.path.exists(upload_file_path):
        os.mkdir(upload_file_path)


def register_host_ip(app, _):
    public_url = ngrok.connect(addr=9090, port=9090, bind_tls=True)
    print(public_url)

def list_upload_files():
    folders = []
    for name in os.listdir(upload_file_path):
        folders.append(name)
    return folders