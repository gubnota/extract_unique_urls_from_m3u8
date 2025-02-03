#!/usr/bin/env python3
import os
import sys

def extract_unique_urls(lines):
    """Extract unique URLs from an m3u8 file in order of appearance."""
    unique_urls = []
    for line in lines:
        line = line.strip()
        if line.startswith('http') or line.startswith('https'):
            line = line.split('?')[0].strip()
            if line not in unique_urls:
                unique_urls.append(line)
    # unique_urls = list(unique_urls)
    # unique_urls.reverse()
    # unique_urls = set(unique_urls)
    return unique_urls

def concatenate_url_downloaded_files(unique_urls, output_file):
    os.system("touch " + output_file)
    for url in unique_urls:
        print(f"url = '{url}'")
        os.system(f"curl '{url}' -o tmp")
        os.system(f"cat tmp >> {output_file}")
        os.system("rm tmp")

def process_m3u8(input_file, output_file):
    if (input_file.endswith('.xz')):
        import lzma
        with lzma.open(input_file, 'rt') as f:
            lines = f.readlines()
    else:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    unique_urls = extract_unique_urls(lines)
    for url in unique_urls:
        print(url)
    concatenate_url_downloaded_files(unique_urls, output_file)

if __name__ == "__main__":
    # Check if curl is available in the system
    if os.system("which curl > /dev/null 2>&1") != 0:
        print("Error: curl is not installed or not available in PATH")
        sys.exit(1)
    if len(sys.argv) != 3:
        print("Usage: python3 download_and_multiplex.py <input_file.m3u8(.xz)> <output_file.m4v|m4a>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f"input_file = {input_file}, output_file = {output_file}")
    process_m3u8(input_file, output_file)
