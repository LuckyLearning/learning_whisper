import whisper

# model = whisper.load_model(name="base", download_root="../models")
#
# rootPath = "../audio/7a11f71b391bb63f9007f0e37601a77d.mp4"
#
# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio(rootPath)
# audio = whisper.pad_or_trim(audio)
#
# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)
#
# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")
#
# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)
#
# # print the recognized text
# print(result.text)

def detect_language(model, filepath):
    audio = whisper.load_audio(filepath)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    return max(probs, key=probs.get)

if __name__ == '__main__':
    pass
    # detect_language(rootPath)