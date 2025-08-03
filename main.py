import os
from extract_audio import extract_audio
from transcribe_audio import transcribe
from generate_subtitles import generate_subtitle_file

input_video = "Vanka.mp4"
base_name = os.path.splitext(input_video)[0]
audio_file = f"{base_name}.wav"
srt_file = f"{base_name}.srt"

# Step 1: Extract audio
extracted_audio = extract_audio(input_video, audio_file)
print("Extracted:", extracted_audio)

# Step 2: Transcribe
language, segments = transcribe(extracted_audio)

# Step 3: Generate subtitles
subtitle_path = generate_subtitle_file(srt_file, segments, language)
print("Subtitle generated at:", subtitle_path)
