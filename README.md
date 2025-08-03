## 🧠🎬 Video Add Subtitle

Automatically extract audio from a video, transcribe it using OpenAI's Whisper (via `faster-whisper`), and generate subtitle files in `.srt` format.

---

### 📂 Project Structure
```
video-subtitle-generator/
├── main.py
├── extract_audio.py
├── transcribe_audio.py
├── generate_subtitles.py
├── requirements.txt
└── README.md
```

---
### ⚙️ Requirements

* Python 3.8+
* FFmpeg installed and added to PATH

---

### 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/video-subtitle-generator.git
cd video-subtitle-generator
```

2. **Create a virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install FFmpeg**

Make sure [FFmpeg](https://ffmpeg.org/download.html) is installed and available in your system's PATH.

---

### 🧪 Usage

1. Place your video file (e.g., `story.mp4`) in the project directory.
2. Run:

```bash
python main.py
```

3. Output:

   * Audio file: `story.wav`
   * Subtitle file: `story.srt`

---

### 🧱 What Each Module Does

* `extract_audio.py` – Extracts mono 16kHz audio from a video using FFmpeg.
* `transcribe_audio.py` – Uses `faster-whisper` to transcribe the audio.
* `generate_subtitles.py` – Generates `.srt` subtitle file from the transcription segments.
* `main.py` – Orchestrates the whole process.

---

### 📌 Example

```text
Detected language: en
[0.00s -> 5.12s] Once upon a time...
[5.12s -> 10.23s] There was a brave coder...

Generated: story.srt
```

---

### 📄 License

MIT License. Do what you want — just give credit if you find it useful. ❤️

---

### 🙌 Contributing

Pull requests and suggestions are welcome. If you find a bug or want to improve something, feel free to open an issue or PR.