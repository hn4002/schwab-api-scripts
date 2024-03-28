#!/opt/homebrew/bin/python3

# This script uses the access token to get the account numbers for the user.

import json
import os
import requests
import sys

# Include local lib code from the project
local_lib_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'lib')
if local_lib_dir not in sys.path:
    sys.path.append(local_lib_dir)
from schwablib.setenv import schwabSettings

access_token = schwabSettings.get_access_token()

#====================================================================================================
def main():
    # Get access_token from the token file
    url = f"https://api.schwabapi.com/trader/v1/accounts/accountNumbers"
    headers = {
        "Accept": "application/json",
        "Schwab-Client-CorrelId": "dummy",
        "Authorization": f"Bearer {access_token}"
    }
    print(f"Calling url: {url}, headers: {headers}")
    response = requests.get(url, headers=headers)
    print(f"response.code is {response.status_code}")
    print(f"response.text is {response.text}")
    # Print headers
    print(f"response.headers are: \n{json.dumps(dict(response.headers), indent=4)}")

    # Save result in the token file
    out_text = json.dumps(response.json(), indent=4)
    print(f"respnose object: \n{out_text}")


#====================================================================================================
if __name__ == "__main__":
    main()
