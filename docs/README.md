# Schwab API

* https://developer.schwab.com/

# Schwab API Status

**Following features are missing**

* Streaming APIs
* Support for Joint Account, IRA, Roth, PCRA

**Folllwing features have been released**

* Authentication APIs (OAuth) and related services
* Account & Order Management APIs
* Market Data APIs
* API access approval (may take couple of weeks) and applicatino approval (take about 3 business days)

# Schwab API Communication Updates

**3/27**

With the Schwab Trader API, refresh tokens are valid for 7 days, or until they are invalidated (i.e. user password reset). 
Once the existing refresh token is no longer valid, 'Refresh Token' (Step 4) will no longer be available. 
To restart the OAuth Flow, both the 'App Authorization' (Step 1) and 'Access Token Creation' (Step 2) steps must be repeated.
This is by design for the Schwab Trader API.

The manual login process is required during the 'Access Token Creation' process, which must be completed in order to restart
the OAuth Flow once an existing refresh token expires (7 calendar days).
There is no workaround or way to bypass this process available for the schwab Trader API, which does differ from TDA legacy API.

**3/26**

Market data documentation will be uploaded to Schwab Developer portal by the end of the month.

Not all account types are going to be initially available with Schwab Trader API, that includes but not limited to HSA, PCRA,
Joint Tennant, Designated Beneficiary Joint Tennant account types. We will work to add support for those accounts in the near
future, no ETA is available yet.

