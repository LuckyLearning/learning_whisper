import logging

import whisper

logger = logging.getLogger(__name__)


def detect_language(model, filepath):
    audio = whisper.load_audio(filepath)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    language = max(probs, key=probs.get)
    logger.debug("模型识别语言：", language)
    return language


if __name__ == '__main__':
    pass
    # detect_language(rootPath)
