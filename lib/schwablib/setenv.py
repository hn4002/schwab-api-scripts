import json
import os


#=====================================================================================
class SchwabSettings(object):

    # ====================================================================================================
    def __init__(self):
        self.SCHWAB_APP_ID = "DUMMYADFAJDFAFDKJFAFHAKF"
        self.SCHWAB_APP_SECRET = "DUMMYABCDEFADFJLAFDA"
        self.SCHWAB_REDIRECT_URI = "https://127.0.0.1:8080"
        self.SCHWAB_TOKEN_PATH = "/usr/local/token.json"
        self.SCHWAB_REFRESH_TOKEN_PATH = "/usr/local/refresh_token.json"

        self.SCHWAB_ACCOUNT_ID = "123456789"

    # ====================================================================================================
    def get_access_token(self):
        access_token = None
        with open(self.SCHWAB_TOKEN_PATH, 'r') as f:
            token_data = json.load(f)
            access_token = token_data["access_token"]
        return access_token


schwabSettings = SchwabSettings()


