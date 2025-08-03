import ffmpeg
import os

def extract_audio(input_video_path: str, output_audio_path: str):
    stream = ffmpeg.input(input_video_path)
    stream = ffmpeg.output(stream, output_audio_path, ac=1, ar='16000')  # mono & 16kHz
    ffmpeg.run(stream, overwrite_output=True)
    return output_audio_path
