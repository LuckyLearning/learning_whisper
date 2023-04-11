import logging
import os.path
from typing import Text

import whisper
from whisper import Whisper

from test_detect import detect_language

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(asctime)s %(filename)s [line:%(lineno)d]] %(levelname)s: %(message)s", level=logging.INFO)

rootPath = None
lng = None

def start():
    logger.info(f"whisper 可用的模型：\n{whisper.available_models()}")
    type = "medium"
    logger.info(f"选择的模型：{type}")
    model: Whisper = loadModel(type)
    language: Text = detect_language(model, rootPath)
    print("模型识别语言：", language)
    lng = language
    transcription = transcribe(model, lng)
    write(transcription, type)


def loadModel(type: Text) -> Whisper:
    logger.info("开始装载模型".center(60, "#"))
    model = whisper.load_model(name=type, download_root="../models")
    logger.info("模型装载完成".center(60, "#"))
    return model


def transcribe(model, lng):
    logger.info(f"指定的语言：{lng}")
    logger.info("开始识别：")
    prompt = '以下是普通话的句子, 隋总'
    result = model.transcribe(audio=rootPath, verbose=True, language=lng, initial_prompt=prompt)
    logger.debug("result debug:\n", result)
    transcription = result["text"]
    return transcription


def write(transcription, type):
    path1 = os.path.splitext(rootPath)[0]
    filename = os.path.split(path1)[-1]
    filepath = f"../result/{filename}-{type}.txt"
    with open(filepath, "w") as f:
        f.write(transcription)
    logger.info(f"写入文件：{filepath}")


if __name__ == '__main__':
    rootPath = "../audio/7a11f71b391bb63f9007f0e37601a77d.mp4"
    start()
