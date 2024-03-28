# Schwab API Scripts
Some scripts to test OAuth flow and functionl APIs in Schwab APIs

The sensitive info has been "externalized" into a different file. The file is `lib/schwablib/setenv.py`. Update it with the right values for your app. Depending on where you put `setenv.py` on your system, update `local_lib_dir` global variable in the other scripts to load it.

The scripts to test the OAUTH flow and to test some functional APIs are in `scripts/schwabScripts` directory.

