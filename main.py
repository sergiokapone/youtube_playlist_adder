import configparser

from auth import authenticate
from youtube_api import (
    create_youtube_client,
    get_playlist_id,
    create_playlist,
    add_video_to_playlist,
    extract_video_id,
)

config = configparser.ConfigParser()
config.read('config.ini')


# Authentication options
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
client_secrets_file = config.get('auth', 'CLIENT_SECRET')
credentials_file = config.get('auth', 'CREDENTIALS')

# Specify a YouTube URL array
urls_file = config.get('settings', 'URLS')
playlist_name = config.get('settings', 'PLAYLIST')

with open(urls_file) as f:
    youtube_urls = f.readlines()



# Authenticating and creating a YouTube API client
credentials = authenticate(scopes, client_secrets_file, credentials_file)
youtube = create_youtube_client("youtube", "v3", credentials)

# Obtaining or creating a playlist
playlist_id = get_playlist_id(youtube, playlist_name)
if not playlist_id:
    playlist_id = create_playlist(youtube, playlist_name)

# Checking for videos in the playlist and adding only missing videos
for url in youtube_urls:
    video_id = extract_video_id(url)
    if video_id:
        add_video_to_playlist(youtube, playlist_id, video_id)
