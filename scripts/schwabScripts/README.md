These are the four scripts in this directory for the initial testing of Schwab API (in that sequence):

# do_app_auth_n_get_refresh_token.py

This script does OAuth2 authorization for the Schwab API.
It uses the app_id and app_secret to do the app authroization and get the refresh token.
The refresh token is saved in the specified file.

# get_access_token.py

This script uses the refresh token to get the access token.
It reads the refresh token from the specified file.
The access token is saved in the specified file.

# get_account_numbers.py

This script uses the access token to get the account numbers for the user.

# get_quote.py

This script uses the access token to get the quote for a symbol.
