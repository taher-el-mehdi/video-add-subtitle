from faster_whisper import WhisperModel

def transcribe(audio_path: str, model_size: str = "small"):
    model = WhisperModel(model_size)
    segments, info = model.transcribe(audio_path)
    language = info.language
    print("Detected language:", language)
    segments = list(segments)
    return language, segments
