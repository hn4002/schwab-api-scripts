#!/opt/homebrew/bin/python3

# This script does OAuth2 authorization for the Schwab API.
# It uses the app_id and app_secret to do the app authroization and get the refresh token.
# The refresh token is saved in the specified file.

import json
import os
import requests
import sys
import urllib.parse as urlparse

# Include local lib code from the project
local_lib_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'lib')
if local_lib_dir not in sys.path:
    sys.path.append(local_lib_dir)
from schwablib.setenv import schwabSettings

client_id = schwabSettings.SCHWAB_APP_ID
client_secret = schwabSettings.SCHWAB_APP_SECRET
redirect_uri = schwabSettings.SCHWAB_REDIRECT_URI
refresh_token_path = schwabSettings.SCHWAB_REFRESH_TOKEN_PATH

#====================================================================================================
def main():
    print(f"App Info:\n    client_id={client_id}\n    client_secret={client_secret}\n    redirect_uri={redirect_uri}")

    # App authorization
    app_auth_url = 'https://api.schwabapi.com/v1/oauth/authorize'
    url = f"{app_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}"
    print(f"\nCalling Url: {url}")
    response = requests.get(url)
    print(f"response.code is {response.status_code}")
    print(f"response.text is {response.text}")
    print(f"response.headers are: \n{json.dumps(dict(response.headers), indent=4)}")
    print("App Authoriztion Url:")
    print(response.url)

    print(f"Paste the url printed above in your browser. Login using the Schwab Brokerage login, accept the 'Trader API End "
          f"User Terms and Conditions' agreement and approve the  accounts.\nOnce it returns back to your callback url, "
          f"copy and paste the full url here quickly and press enter.\nRedirected url: ")
    redirect_url_with_token = input()

    print(f"Read url from input = {redirect_url_with_token}")
    # Get the auth code and session id from the url
    parsed_url = urlparse.urlparse(redirect_url_with_token)
    print(f"query = {parsed_url.query}")
    parsed_query = urlparse.parse_qs(parsed_url.query)
    print(f"parsed_query = {parsed_query}")
    auth_code = parsed_query['code'][0]
    session_id = parsed_query['session'][0]
    print(f"auth_code={auth_code}, session_id={session_id}")

    token_url = 'https://api.schwabapi.com/v1/oauth/token'
    data = {
        'grant_type' : 'authorization_code',
        'code' : auth_code,
        'client_id' : client_id,
        'redirect_uri' : redirect_uri
    }
    print(f"\nCalling Url: {token_url}")
    response = requests.post(token_url, auth=(client_id, client_secret), data = data)
    print(f"response.code is {response.status_code}")
    print(f"response.text is {response.text}")
    print(f"response.headers are: \n{json.dumps(dict(response.headers), indent=4)}")

    # Save result in the token file
    out_text = json.dumps(response.json(), indent=4)
    print(f"respnose object: \n{out_text}")
    with open(refresh_token_path, 'w') as f:
        f.write(out_text)
    print(f"Refresh token saved in file: {refresh_token_path}")

#====================================================================================================
if __name__ == "__main__":
    main()
