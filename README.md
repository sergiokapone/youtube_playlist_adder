# YouTube Playlist Adder

`YouTube Playlist Adder` is a Python script that allows you to create and manage playlists on YouTube by adding videos from a list of URLs. It uses the YouTube `Data API v3` to interact with the YouTube service.

## Features

- Authenticate with your YouTube account using OAuth 2.0.
- Create a new playlist or choose an existing playlist on your YouTube account.
- Load a list of video URLs from a text file.
- Add videos to the selected playlist, skipping duplicates.
- Customize the playlist title and description.

## Installation

1. Clone or download the repository to your local machine.

```bash
git clone https://github.com/sergiokapone/youtube_playlist_adder.git
```

2. Install the required dependencies by running `pipenv install`.
3. Obtain the client secrets file (`client_secret.json`) for your `YouTube API` project and place it in the project directory.
4. Make sure you have a text file containing the list of video URLs (one URL per line) that you want to add to the playlist.

## Usage

1. Open the `config.ini` file and set the desired playlist name (`PLAYLIST`) and the path to the text file containing the video URLs (`URLS`).
2. Run the `main.py` script using `python main.py`.
3. The script will prompt you to authenticate with your YouTube account if necessary. Follow the instructions in the console to complete the authentication process.
4. The script will create the playlist (if it doesn't exist) or use the existing playlist with the specified name.
5. It will then add the videos from the URL list to the playlist, skipping any duplicates.
6. You will see the status of each video being added or skipped in the console output.

Note: The script uses `OAuth 2.0` to authenticate with the YouTube API, so you will need to have a Google account and create a `YouTube API` project in the Google Developer Console to obtain the necessary credentials.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions

Contributions to improve and expand the functionality of the YouTube Playlist Adder are welcome. Feel free to open issues and submit pull requests to contribute to this project.

## Disclaimer

This project is intended for educational and personal use only. The developer assumes no responsibility for any misuse or violation of YouTube's terms of service. Use it responsibly and respect the rights of content creators.
