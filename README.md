# YouTube Playlist Adder <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>  

`YouTube Playlist Adder` is a Python script that allows you to create and manage playlists on YouTube by adding videos from a list of URLs using command line interface. It uses the YouTube `Data API v3` to interact with the YouTube service.

## Features

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

1. Ensure that you have a valid `client_secret.json` file in the project directory. If not, follow the instructions in the "Authentication" section below to obtain the required credentials.
2. Populate the text file with the YouTube video URLs you want to add to the playlist. Each URL should be on a new line.

Example of `urls.txt`:

```text
https://www.youtube.com/watch?v=VD8Xpl1_OM0
https://www.youtube.com/watch?v=JOzhL0Y1GAE
```

4. Run the `main.py` script using the following command-line options:

- `--download` or `-d`: Downloads the videos from the playlist to a file.
- `--upload` or `-u`: Uploads videos from a file to the playlist.
- `--playlist` or `-p`: Specifies the playlist name to use.

Example usage:

To download videos from the playlist with name `MyPlaylist` to a file `urls.txt`:

```shell
python main.py -p MyPlaylist -d urls.txt
```

To upload videos from a file with name `MyPlaylist` to a file `urls.txt`:

```shell
python main.py -p MyPlaylist -u urls.txt
```

5. The script will prompt you to authenticate with your YouTube account if necessary. Follow the instructions in the console to complete the authentication process.
6. The script will create the playlist (if it doesn't exist) or use the existing playlist with the specified name.
7. It will then add the videos from the URL list to the playlist, skipping any duplicates.
8. You will see the status of each video being added or skipped in the console output.

## Authentication procedure

To authenticate with the YouTube API and obtain the necessary credentials, follow these steps:

1. Create a project in the [Google Developer Console](https://console.developers.google.com/):

- Sign in with your Google account or create a new account if needed.
- Click on the "Select a project" dropdown at the top of the page and click the "+ New Project" button.
- Enter a name for your project and click the "Create" button.

2. Enable the YouTube Data API for your project:

- In the Google Developer Console, navigate to your project by clicking on the project name in the top bar.
- On the left sidebar, click on "APIs & Services" and then "Library".
- Search for "YouTube Data API" and click on it in the results.
- Click the "Enable" button to enable the API for your project.

3. Create credentials for the project and download the `client_secret.json` file:

- In the Google Developer Console, navigate to your project by clicking on the project name in the top bar.
- On the left sidebar, click on "APIs & Services" and then "Credentials".
- Click the "+ Create Credentials" button and select "OAuth client ID" from the dropdown.
- Select "Web application" as the application type.
- Enter a name for the OAuth 2.0 client ID.
- In the "Authorized JavaScript origins" field, enter the URL `http://localhost:8080` (if running locally) or the URL of your deployed application.
- In the "Authorized redirect URIs" field, enter the URL `http://localhost:8080/authorized` (if running locally) or the URL of your deployed application followed by `/authorized`.
- Click the "Create" button to create the OAuth client ID.
- On the next screen, you'll see your newly created OAuth client ID along with the client ID and client secret. Make a note of these as they will be used in your authentication process.
- Click the "OK" button to close the dialog.
- Click the download icon next to your client ID to download the `client_secret.json` file. Save this file in the project directory.

4. Place the `client_secret.json` file in the project directory:

- After downloading the `client_secret.json` file, place it in the project directory where the `main.py` script is located.

5. Run the `main.py` script. It will guide you through the authentication process and generate the `credentials.pickle` file.

Note: The `credentials.pickle` file will be used for subsequent authentication to avoid the need to authenticate every time you run the script.

## Quota Limits

The YouTube Data API enforces certain quota limits to prevent abuse and ensure fair usage. Quota limits define the maximum number of requests your application can make to the API within a specific time period. If you exceed these limits, the API will return a 403 Forbidden error with the message "The request cannot be completed because you have exceeded your quota."

If you encounter a 403 Forbidden error with the quotaExceeded reason, you will need to wait until your quota resets or your request for additional quota is approved.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions

Contributions to improve and expand the functionality of the YouTube Playlist Adder are welcome. Feel free to open issues and submit pull requests to contribute to this project.

## Disclaimer

This project is intended for educational and personal use only. The developer assumes no responsibility for any misuse or violation of YouTube's terms of service. Use it responsibly and respect the rights of content creators.
