import subprocess
from pathlib import Path

def create_clip(input_video, start, duration, output):
    if not Path(input_video).is_file():
        print("Error: Video not found!")
        return

    command = [
        "ffmpeg",
        "-y",
        "-ss", str(start),
        "-i", input_video,
        "-t", str(duration),
        "-c:v", "libx264",
        "-c:a", "aac",
        output
    ]

    subprocess.run(command, check=True)
    print("Clip successfully created:", output)


if __name__ == "__main__":
    create_clip(
        "video.mp4",
        30,
        20,
        "clip1.mp4"
    )
