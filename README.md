# MM Lab Projects

This repository contains five Multimedia Lab projects:

1. Image Metadata Analyzer
2. Video Metadata Analyzer
3. Audio Metadata Analyzer
4. Voice Cloning using F5-TTS
5. Image Enhancement

## Folder Structure

- `Image-Metadata-Analyzer/`
- `Video-Metadata-Analyzer/`
- `Audio-Metadata-Analyzer/`
- `Voice-Cloning/`
- `Image-Enhancement/`

Each project is intended to contain its code, one sample input, and the generated output.

## Requirements

Install Python packages:

```bash
pip install -r requirements.txt
```

The Audio and Video analyzers also require **FFmpeg/ffprobe** to be installed and available in PATH.

Voice Cloning uses the **F5-TTS** model. Use only your own voice or a voice you have permission to clone.

## Running

Open a terminal in the relevant project folder and run the Python file, for example:

```bash
python image_analyzer.py
```

Then provide the requested input file path.
