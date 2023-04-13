import logging
import os.path
from typing import Text

import whisper
from whisper import Whisper
from whisper.utils import format_timestamp

from src.util import get_download_model_path, get_result_path, get_upload_file_path

logger = logging.getLogger(__name__)

rootPath = None
lng = None


async def start_trans(filename, modleType, lng):
    logger.debug(f"whisper 可用的模型：\n{whisper.available_models()}")
    if not modleType:
        logger.debug("未指定模型，使用默认模型：tiny")
        modleType = "tiny"
    logger.debug(f"选择的模型：{modleType}")
    model: Whisper = loadModel(modleType)
    if not lng:
        logger.debug("未指定语言，使用默认语言：zh")
        lng = "zh"
    filePath = os.path.join(get_upload_file_path(), filename)
    text, segments = transcribe(filePath, model, lng)
    write(filename, segments, modleType)
    return text


def loadModel(type: Text) -> Whisper:
    logger.debug("开始装载模型".center(60, "#"))
    model = whisper.load_model(name=type, download_root=get_download_model_path())
    logger.debug("模型装载完成".center(60, "#"))
    return model


def transcribe(filePath, model, lng):
    logger.info(f"指定的语言：{lng}")
    logger.info("开始识别：")
    prompt = '以下是普通话的句子'
    result = model.transcribe(audio=filePath, language=lng, initial_prompt=prompt)
    text = result["text"]
    segments = result['segments']
    return text, segments


def write(filename, segments, type):
    result_path = get_result_path()
    filepath = f"{result_path}/{filename}-{type}.txt"
    if os.path.exists(filepath):
        os.remove(filepath)
    for segment in segments:
        with open(filepath, "a") as f:
            start, end, text = segment["start"], segment["end"], segment["text"]
            line = f"[{format_timestamp(start)} --> {format_timestamp(end)}] {text}\n"
            f.write(line)
    logger.info(f"写入文件：{filepath}")
