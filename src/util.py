import logging
import os

import yaml

logger = logging.getLogger(__name__)


def get_root_path():
    abs_path = os.path.abspath(__file__)
    base_path = os.path.dirname(abs_path)
    return os.path.abspath(os.path.join(base_path, "../"))


def load_yaml():
    filepath = os.path.join(get_root_path(), "config.yml")
    if not os.path.exists(filepath):
        msg = f"文件不存在：{filepath}"
        logger.error(msg)
        raise FileNotFoundError(msg)

    with open(filepath, encoding="utf8") as f:
        config = yaml.safe_load(f)
        return config


def get_upload_file_path():
    config = load_yaml()
    upload_file_path = config["upload"]
    if not upload_file_path:
        upload_file_path = "upload"
    return os.path.join(get_root_path(), upload_file_path)


def get_download_model_path():
    config = load_yaml()
    download_model_path = config["models"]
    if not download_model_path:
        download_model_path = "models"
    return os.path.join(get_root_path(), download_model_path)


def get_result_path():
    config = load_yaml()
    result_path = config["result"]
    if not result_path:
        result_path = "result"
    return os.path.join(get_root_path(), result_path)


def get_ngrok_auth():
    config = load_yaml()
    return config["ngrok"]


def list_upload_files():
    folders = []
    for name in os.listdir(get_upload_file_path()):
        if name.endswith(".md"):
            continue
        folders.append(name)
    return folders
