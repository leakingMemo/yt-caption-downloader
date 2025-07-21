#!/usr/bin/env python3
import sys
import os
import yt_dlp
from urllib.parse import urlparse, parse_qs
import argparse

def get_video_id(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query).get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
    elif parsed_url.hostname in ['youtu.be', 'www.youtu.be']:
        return parsed_url.path[1:]
    elif parsed_url.hostname == 'm.youtube.com':
        return parse_qs(parsed_url.query).get('v', [None])[0]
    return None

def fetch_captions(url, output_dir='.', lang='en', format='vtt'):
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': [lang],
        'subtitlesformat': format,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_title = info.get('title', 'Unknown')
            video_id = get_video_id(url) or info.get('id', 'unknown')
            
            subtitle_files = []
            for file in os.listdir(output_dir):
                if file.endswith(f'.{lang}.{format}') or file.endswith(f'.{format}'):
                    subtitle_files.append(file)
            
            if subtitle_files:
                print(f"✅ Successfully downloaded captions for: {video_title}")
                print(f"📁 Saved to: {output_dir}")
                for file in subtitle_files:
                    print(f"   - {file}")
                return True
            else:
                print(f"❌ No captions found for language '{lang}' in video: {video_title}")
                return False
                
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Download YouTube video captions')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-o', '--output', default='.', help='Output directory (default: current directory)')
    parser.add_argument('-l', '--language', default='en', help='Caption language code (default: en)')
    parser.add_argument('-f', '--format', default='vtt', choices=['vtt', 'srt', 'ass', 'lrc', 'json3'], 
                        help='Caption format (default: vtt)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    
    fetch_captions(args.url, args.output, args.language, args.format)

if __name__ == "__main__":
    main()