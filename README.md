# schwab-api-scripts
Some scripts to test Schwab APIs

lib/schwablib/setenv.py has "externalized" configs which need to be updated. Depending on where you put setenv.py on your system, update 'local_lib_dir' in the other scripts to load it.

These are the four scripts in the 'scripts/schwabScripts' directory for the initial testing of Schwab API (in that sequence):

# get_token.py

This script does OAuth2 authorization for the Schwab API. 
It uses the app_id and app_secret to get the refresh token. 
The refresh token is saved in the specified file.

# refresh_token.py

This script uses the refresh token to get the access token.
It reads the refresh token from the specified file.
The access token is saved in the specified file.

# get_account_numbers.py

This script uses the access token to get the account numbers for the user.

# get_quote.py

This script uses the access token to get the quote for a symbol.
