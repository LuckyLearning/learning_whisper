import logging

from sanic import Sanic, json

from trans import start
from util import ensure_upload_path, register_host_ip, list_upload_files

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(asctime)s %(filename)s [line:%(lineno)d]] %(levelname)s: %(message)s",
                    level=logging.DEBUG)

upload_file_path = "../upload/"

app = Sanic("whisper")


@app.post("/upload")
async def upload(request):
    file = request.files.get('file')
    filePath = upload_file_path + file.name
    with open(filePath, "wb") as f:
        f.write(file.body)
    transcription = await start(filePath)
    return json({"status": 200, "message": transcription}, ensure_ascii=False,
                content_type='application/json;charset=utf-8')


@app.get("/listfile")
async def list(request):
    files = list_upload_files()
    return json({"status": 200, "message": files}, ensure_ascii=False,
                content_type='application/json;charset=utf-8')


@app.get("/check")
async def check(request):
    return json({"status": 200, "message": "check"}, ensure_ascii=False,
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
