import logging
import os

from flask import Flask, request, render_template

from src.trans import start_trans
from src.util import get_upload_file_path

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(asctime)s %(filename)s [line:%(lineno)d]] %(levelname)s: %(message)s",
                    level=logging.INFO)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
async def upload():
    modleType = request.args.get("model")
    lng = request.args.get("lng")
    file = request.files.get('file')
    filePath = os.path.join(get_upload_file_path(), file.filename)
    text = ''
    if file:
        file.save(filePath)
        text = await start_trans(file.filename, modleType, lng)
    return text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9080)
