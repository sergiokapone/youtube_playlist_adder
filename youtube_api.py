import os
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs


def create_youtube_client(api_service_name, api_version, credentials):
    # Create a YouTube API client
    youtube = build(api_service_name, api_version, credentials=credentials)
    return youtube


def get_playlist_id(youtube, playlist_name):
    # Get the playlist ID by name
    playlists_response = youtube.playlists().list(part="snippet", mine=True).execute()
    playlists = playlists_response.get("items", [])
    playlist_id = None
    for playlist in playlists:
        if playlist["snippet"]["title"] == playlist_name:
            playlist_id = playlist["id"]
            break
    return playlist_id


def create_playlist(youtube, playlist_name):
    # Create a playlist if it doesn't exist
    playlist_response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": playlist_name,
                "description": "Playlist created by YouTube Playlist Adder"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    ).execute()
    playlist_id = playlist_response["id"]
    return playlist_id


def add_video_to_playlist(youtube, playlist_id, video_id):
    # Add a video to the playlist
    playlist_items_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        videoId=video_id
    ).execute()
    if not playlist_items_response.get("items"):
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        ).execute()
        print(f"Video with ID {video_id} has been successfully added to the playlist.")
    else:
        print(f"Video with ID {video_id} is already in the playlist.")


def extract_video_id(url):
    # Extract video ID from URL
    parsed_url = urlparse(url)
    if parsed_url.netloc == "youtu.be":
        video_id = os.path.split(parsed_url.path)[1]
    else:
        video_id = parse_qs(parsed_url.query).get("v")
        if video_id:
            video_id = video_id[0]
    return video_id


def get_playlist_videos(youtube, playlist_id):
    videos = []
    next_page_token = None

    while True:
        playlist_items_response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        items = playlist_items_response.get("items", [])
        for item in items:
            video_id = item["contentDetails"]["videoId"]
            videos.append(video_id)

        next_page_token = playlist_items_response.get("nextPageToken")

        if not next_page_token:
            break

    return videos
