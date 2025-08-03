import re

def format_time(seconds: float) -> str:
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

def clean_text(text: str) -> str:
    # Remove common punctuation (add/remove as needed)
    return re.sub(r"[.,;:!?]", "", text).strip()
    
def generate_subtitle_file(output_path: str, segments, language: str = "en"):
    text = ""
    for index, segment in enumerate(segments):
        segment_start = format_time(segment.start)
        segment_end = format_time(segment.end)
        cleaned = clean_text(segment.text)
        text += f"{index + 1}\n"
        text += f"{segment_start} --> {segment_end}\n"
        text += f"{cleaned}\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path
