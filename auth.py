import pickle
from google_auth_oauthlib.flow import InstalledAppFlow


def authenticate(scopes, client_secrets_file, credentials_file):
    # Checking for saved credentials
    try:
        # Downloading saved credentials
        with open(credentials_file, "rb") as creds_file:
            credentials = pickle.load(creds_file)
        # Проверка срока действия учетных данных
        if credentials and credentials.valid:
            print("Saved credentials are used.")
        else:
            raise ValueError
    except (IOError, ValueError):
        # If the saved credentials are not found or have expired, start the authentication process
        print("Требуется аутентификация.")
        # Create an OAuth Flow
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_local_server(port=0)
        # Save credentials
        with open(credentials_file, "wb") as creds_file:
            pickle.dump(credentials, creds_file)
    
    return credentials
