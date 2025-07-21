# YouTube Caption Downloader

A simple command-line tool to download captions/subtitles from YouTube videos using yt-dlp.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/leakingMemo/yt-caption-downloader.git
cd yt-caption-downloader
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

3. Make the script executable:
```bash
chmod +x yt_captions.py
```

4. (Optional) Create a global command:
```bash
# Create a wrapper script in your PATH
echo '#!/bin/bash
cd /path/to/yt-caption-downloader
python3 yt_captions.py "$@"' > ~/.local/bin/yt-captions
chmod +x ~/.local/bin/yt-captions
```

## Usage

```bash
# Basic usage
python3 yt_captions.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Or if you created the global command
yt-captions "https://www.youtube.com/watch?v=VIDEO_ID"

# Specify output directory
yt-captions "https://www.youtube.com/watch?v=VIDEO_ID" -o ./subtitles

# Download in different language (e.g., Spanish)
yt-captions "https://www.youtube.com/watch?v=VIDEO_ID" -l es

# Download in different format (default is vtt)
yt-captions "https://www.youtube.com/watch?v=VIDEO_ID" -f srt
```

## Options

- `-o, --output`: Output directory (default: current directory)
- `-l, --language`: Caption language code (default: en)
- `-f, --format`: Caption format - vtt, srt, ass, lrc, json3 (default: vtt)

## Supported Formats

- **vtt**: WebVTT format (default)
- **srt**: SubRip format
- **ass**: Advanced SubStation Alpha
- **lrc**: LRC lyrics format
- **json3**: JSON format

## Requirements

- Python 3.6+
- yt-dlp

## License

MIT