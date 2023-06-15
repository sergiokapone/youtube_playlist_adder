import logging
import argparse
import configparser
import json

import colorlog

from auth import authenticate
from youtube_api import (
    create_youtube_client,
    get_playlist_id,
    create_playlist,
    add_video_to_playlist,
    extract_video_id,
    get_playlist_videos,
)

from googleapiclient.errors import HttpError

color_formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)


console_handler = logging.StreamHandler()
console_handler.setFormatter(color_formatter)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)



config = configparser.ConfigParser()
config.read('config.ini')

# Parse command-line arguments
parser = argparse.ArgumentParser(description='YouTube Playlist Adder')

parser.add_argument('--download', '-d', metavar='FILENAME',
                    help='Download videos from playlist to a file')

parser.add_argument('--upload', '-u', metavar='FILENAME',
                    help='Upload videos from a file to playlist')

parser.add_argument('--playlist', '-p', metavar='PLAYLIST_NAME', help='Playlist name')

args = parser.parse_args()

# Authentication options
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
client_secrets_file = config.get('auth', 'CLIENT_SECRET')
credentials_file = config.get('auth', 'CREDENTIALS')

# Specify a YouTube URL array
playlist_name = args.playlist

# Authenticating and creating a YouTube API client
credentials = authenticate(scopes, client_secrets_file, credentials_file)
youtube = create_youtube_client("youtube", "v3", credentials)

try:

    # Obtaining or creating a playlist
    playlist_id = get_playlist_id(youtube, playlist_name)
    if not playlist_id:
        playlist_id = create_playlist(youtube, playlist_name)

    # Downloading videos from playlist to a file
    if args.download:
        playlist_videos = get_playlist_videos(youtube, playlist_id)
        with open(args.download, 'w') as f:
            for video in playlist_videos:
                url = f"https://www.youtube.com/watch?v={video}"
                f.write(url + '\n')
        logger.info(f"Videos downloaded successfully to {args.download}")

    # Uploading videos from a file to playlist
    if args.upload:
        with open(args.upload) as f:
            youtube_urls = f.readlines()
        for url in youtube_urls:
            video_id = extract_video_id(url)
            if video_id:
                add_video_to_playlist(youtube, playlist_id, video_id)
        logger.info(f"Videos uploaded successfully from {args.upload} to playlist")

except HttpError as e:
    error_response = json.loads(e.content.decode("utf-8"))
    error_code = error_response.get('error', {}).get('code')
    logger.error(f"""An error occurred. Error code: {error_code}. The request cannot be completed because you have exceeded your quota.""")