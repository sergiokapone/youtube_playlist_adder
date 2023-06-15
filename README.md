# YouTube Playlist Adder

`YouTube Playlist Adder` is a Python script that allows you to create and manage playlists on YouTube by adding videos from a list of URLs. It uses the YouTube `Data API v3` to interact with the YouTube service.

## Features

- Authenticate with your YouTube account using `OAuth 2.0`.
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
2. Ensure that you have a valid `client_secret.json` file and a `credentials.pickle` file in the project directory. If not, follow the instructions in the "Authentication" section below to obtain the required credentials.
3. Populate the text file specified in `URLS` with the YouTube video URLs you want to add to the playlist. Each URL should be on a new line.

Example of `urls.txt`:

```text
https://www.youtube.com/watch?v=VD8Xpl1_OM0
https://www.youtube.com/watch?v=JOzhL0Y1GAE
```

4. Run the `main.py` script using `python main.py`.
5. The script will prompt you to authenticate with your YouTube account if necessary. Follow the instructions in the console to complete the authentication process.
6. The script will create the playlist (if it doesn't exist) or use the existing playlist with the specified name.
7. It will then add the videos from the URL list to the playlist, skipping any duplicates.
8. You will see the status of each video being added or skipped in the console output.

## Authentication procedure

To authenticate with the YouTube API and obtain the necessary credentials, follow these steps:

1. Create a project in the [Google Developer Console](https://console.developers.google.com/).
2. Enable the YouTube Data API for your project.
3. Create credentials for the project and download the `client_secret.json` file.
4. Place the `client_secret.json` file in the project directory.
5. Run the `main.py` script. It will guide you through the authentication process and generate the `credentials.pickle` file.

Note: The `credentials.pickle` file will be used for subsequent authentication to avoid the need to authenticate every time you run the script.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions

Contributions to improve and expand the functionality of the YouTube Playlist Adder are welcome. Feel free to open issues and submit pull requests to contribute to this project.

## Disclaimer

This project is intended for educational and personal use only. The developer assumes no responsibility for any misuse or violation of YouTube's terms of service. Use it responsibly and respect the rights of content creators.
