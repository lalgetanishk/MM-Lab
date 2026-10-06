import json
import os
import subprocess

def format_size(size_bytes):
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes / (1024 * 1024):.2f} MB"

def run_ffprobe(file_path):
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format", "-show_streams",
        file_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)

def analyze_video(video_path):
    if not os.path.isfile(video_path):
        raise FileNotFoundError("Video file does not exist.")

    data = run_ffprobe(video_path)
    fmt = data.get("format", {})
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), {})
    audio = next((s for s in streams if s.get("codec_type") == "audio"), {})

    fps = video.get("avg_frame_rate", "N/A")
    duration = fmt.get("duration", "N/A")

    lines = [
        "=" * 42,
        "VIDEO METADATA REPORT",
        "=" * 42,
        f"File Name       : {os.path.basename(video_path)}",
        f"File Size       : {format_size(os.path.getsize(video_path))}",
        f"Container       : {fmt.get('format_long_name', fmt.get('format_name', 'N/A'))}",
        f"Duration        : {duration} seconds",
        "",
        "VIDEO",
        "-" * 42,
        f"Resolution      : {video.get('width', 'N/A')} x {video.get('height', 'N/A')}",
        f"Frame Rate      : {fps}",
        f"Bit Rate        : {video.get('bit_rate', fmt.get('bit_rate', 'N/A'))}",
        f"Codec           : {video.get('codec_long_name', video.get('codec_name', 'N/A'))}",
        "",
        "AUDIO",
        "-" * 42,
        f"Codec           : {audio.get('codec_long_name', audio.get('codec_name', 'N/A'))}",
        f"Channels        : {audio.get('channels', 'N/A')}",
        f"Sampling Rate   : {audio.get('sample_rate', 'N/A')} Hz",
        f"Bit Rate        : {audio.get('bit_rate', 'N/A')}",
        "",
        "METADATA",
        "-" * 42,
    ]

    tags = fmt.get("tags", {})
    if tags:
        for key, value in tags.items():
            lines.append(f"{key:<16}: {value}")
    else:
        lines.append("No additional metadata found.")

    report = "\n".join(lines)
    print(report)

    with open("video_output.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("\nReport saved as video_output.txt")

if __name__ == "__main__":
    path = input("Enter video path: ").strip().strip('"')
    try:
        analyze_video(path)
    except FileNotFoundError as e:
        print("Error:", e)
    except subprocess.CalledProcessError:
        print("Error: ffprobe could not analyze this file.")
    except Exception as e:
        print("Error:", e)
