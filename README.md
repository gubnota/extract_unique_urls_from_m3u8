# What is this?
`extract_unique_urls_from_m3u8` searches unique urls from m3u8 file, downloads chunks, combine them into one m4a or m4v (typically) or ts file.

## Alternatives
```sh
ffmpeg -i "URL_for_video_720p_or_audio_stream.m3u8" -c copy -bsf:a aac_adtstoasc "output.mp4"
```

## Install and usage
1. Download some m3u8 files
2. use poetry or uv to install dependencies
```sh
poetry install
```
3. run the script
```sh
poetry run python main.py
```
