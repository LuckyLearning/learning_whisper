import logging
import os.path
from typing import Text

import whisper
from whisper import Whisper
from whisper.utils import format_timestamp

logger = logging.getLogger(__name__)

rootPath = None
lng = None


async def start(filePath):
    logger.debug(f"whisper 可用的模型：\n{whisper.available_models()}")
    type = "medium"
    logger.debug(f"选择的模型：{type}")
    model: Whisper = loadModel(type)
    lng = "zh"
    transcription, segments = transcribe(filePath, model, lng)
    write(filePath, segments, type)
    return transcription, segments


def loadModel(type: Text) -> Whisper:
    logger.debug("开始装载模型".center(60, "#"))
    model = whisper.load_model(name=type, download_root="../models")
    logger.debug("模型装载完成".center(60, "#"))
    return model


def transcribe(filePath, model, lng):
    logger.info(f"指定的语言：{lng}")
    logger.info("开始识别：")
    prompt = '以下是普通话的句子'
    result = model.transcribe(audio=filePath, language=lng, initial_prompt=prompt)
    transcription = result["text"]
    segments = result['segments']
    return transcription, segments


def write(filePath, segments, type):
    path1 = os.path.splitext(filePath)[0]
    filename = os.path.split(path1)[-1]
    filepath = f"../result/{filename}-{type}.txt"
    if os.path.exists(filepath):
        os.remove(filepath)
    for segment in segments:
        with open(filepath, "a") as f:
            start, end, text = segment["start"], segment["end"], segment["text"]
            line = f"[{format_timestamp(start)} --> {format_timestamp(end)}] {text}\n"
            f.write(line)
    logger.info(f"写入文件：{filepath}")
