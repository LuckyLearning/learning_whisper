import logging
import os

from sanic import Sanic, json

from src.detect import start_detect
from src.ensurepath import ensure_upload_path
from src.ngrok import register_host_ip
from src.trans import start_trans
from src.util import get_upload_file_path, list_upload_files

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(asctime)s %(filename)s [line:%(lineno)d]] %(levelname)s: %(message)s",
                    level=logging.DEBUG)

app = Sanic("whisper")


@app.post("/detect")
async def detect(request):
    modleType = request.args.get("model")
    file = request.files.get('file')
    filePath = os.path.join(get_upload_file_path(), file.name)
    with open(filePath, "wb") as f:
        f.write(file.body)
    lng = await start_detect(filePath, modleType)
    return json({"status": 200, "message": lng}, ensure_ascii=False,
                content_type='application/json;charset=utf-8')


@app.post("/trans")
async def trans(request):
    modleType = request.args.get("model")
    lng = request.args.get("lng")
    file = request.files.get('file')
    filePath = os.path.join(get_upload_file_path(), file.name)
    with open(filePath, "wb") as f:
        f.write(file.body)
    text = await start_trans(file.name, modleType, lng)
    return json({"status": 200, "message": text}, ensure_ascii=False,
                content_type='application/json;charset=utf-8')


@app.get("/listfile")
async def list(request):
    files = list_upload_files()
    return json({"status": 200, "message": files}, ensure_ascii=False,
                content_type='application/json;charset=utf-8')


@app.get("/")
async def hello(request):
    return json({"status": 200, "message": "hello"}, ensure_ascii=False,
                content_type='application/json;charset=utf-8')


app.register_listener(ensure_upload_path, "after_server_start")
app.register_listener(register_host_ip, "after_server_start")

if __name__ == '__main__':
    port = 9090
    app.run(host="0.0.0.0", port=port, workers=1)
