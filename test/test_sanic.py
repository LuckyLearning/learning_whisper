import os
from sanic import Sanic, json

upload_file_path = "../upload/"

app = Sanic("whisper")

@app.post("/whisper/upload")
async def upload(request):
    file = request.files.get('file')
    with open(upload_file_path + file.name, "wb") as f:
        f.write(file.body)
    print("#"*80)
    return json({"status": 200, "message": "OK"}, ensure_ascii=False, content_type='application/json;charset=utf-8')


if __name__ == '__main__':
    if not os.path.exists(upload_file_path):
        os.mkdir(upload_file_path)
    app.run(host="0.0.0.0", port=9090)