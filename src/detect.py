import logging
from typing import Text

import whisper
from whisper import Whisper

logger = logging.getLogger(__name__)


async def start_detect(filePath, modleType):
    logger.debug(f"whisper 可用的模型：\n{whisper.available_models()}")
    if not modleType:
        logger.debug("未指定模型，使用默认模型：tiny")
        modleType = "tiny"
    logger.debug(f"选择的模型：{modleType}")
    model: Whisper = loadModel(modleType)
    return detect_language(model, filePath)


def loadModel(type: Text) -> Whisper:
    logger.debug("开始装载模型".center(60, "#"))
    model = whisper.load_model(name=type, download_root="../models")
    logger.debug("模型装载完成".center(60, "#"))
    return model


def detect_language(model, filepath):
    audio = whisper.load_audio(filepath)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    language = max(probs, key=probs.get)
    logger.info(f"模型识别语言：{language}")
    return language
