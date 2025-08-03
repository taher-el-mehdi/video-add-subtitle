import ffmpeg

def add_subtitles_to_video(input_video_path: str, subtitle_path: str, output_video_path: str):
    try:
        (
            ffmpeg
            .input(input_video_path)
            .output(output_video_path, vf=f"subtitles={subtitle_path}")
            .overwrite_output()
            .run()
        )
        print(f"Subtitled video saved to: {output_video_path}")
        return output_video_path
    except ffmpeg.Error as e:
        print("FFmpeg error:", e.stderr.decode())
        return None
