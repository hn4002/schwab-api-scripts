#!/opt/homebrew/bin/python3

# This script uses the refresh token to get the access token.
# It reads the refresh token from the specified file.
# The access token is saved in the specified file.

import base64
import json
import os
import requests
import sys

# Include local lib code from the project
local_lib_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'lib')
if local_lib_dir not in sys.path:
    sys.path.append(local_lib_dir)
from schwablib.setenv import schwabSettings

client_id = schwabSettings.SCHWAB_APP_ID
client_secret = schwabSettings.SCHWAB_APP_SECRET
token_path = schwabSettings.SCHWAB_TOKEN_PATH
refresh_token_path = schwabSettings.SCHWAB_REFRESH_TOKEN_PATH

#====================================================================================================
def main():
    # Load refresh token from file
    refresh_token_data = None
    with open(refresh_token_path, 'r') as f:
        refresh_token_data = json.load(f)
    refresh_token = refresh_token_data["refresh_token"]
    print(f"refresh_token is {refresh_token}")

    print(f"App Info:\n    client_id={client_id}\n    client_secret={client_secret}")
    auth_raw_string = f"{client_id}:{client_secret}"
    print(f"auth_raw_string is {auth_raw_string}")
    basic_auth_header = base64.b64encode(auth_raw_string.encode()).decode()
    print(f"basic_auth_header is {basic_auth_header}")

    print(f"token_path is {token_path}")
    # Remove token file
    if os.path.exists(token_path):
        os.remove(token_path)

    url = "https://api.schwabapi.com/v1/oauth/token"
    headers = {
        "Authorization": f"Basic {basic_auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    response = requests.post(url, headers=headers, data=data)
    print(f"response.code is {response.status_code}")
    print(f"response.text is {response.text}")
    # Print headers
    print(f"response.headers are: \n{json.dumps(dict(response.headers), indent=4)}")

    # Save result in the token file
    out_text = json.dumps(response.json(), indent=4)
    print(f"respnose object: \n{out_text}")
    with open(token_path, 'w') as f:
        f.write(out_text)
    print(f"Token data written to {token_path}")

#====================================================================================================
if __name__ == "__main__":
    main()


