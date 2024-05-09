# Schwab API

* https://developer.schwab.com/

# Status

**Following TDA API features have not been released by Schwab API team**

* Streaming APIs

**Folllwing features have been released**

* Authentication APIs (OAuth) and related services
* Account & Order Management APIs
* Market Data APIs
* API access approval (takes about 5 business days) and the application approval (takes about 3 business days)
* Support for joint accounts and authorized accounts

# Known Issues

These are the current known issues. Hopefully the API team can fix these bugs on a timely manner.

1. The order management APIs currently do not work well with ETFs. Once a order is created for an ETF, the get order or the get transaction does not include 'symbol' information.


# FAQ

**Is there any rate limit**

I just called get_quote api 300 times. I didn't notice any rate limit. It took 68.47 secs. 228 ms/call. 22 ms is latency to api.schwabapi.com from my computer, so they are taking 206 ms to process request for get_quote.  

We should code our app to expect rate limit.  The Schwab API team is lagging on adding the features itself, so they may not have time to add rate limit to their APIs yet.


# Troubleshooting

**Q: Application creation failure**

1. Make sure you are not putting "/" at the end of the callback url.
2. Make sure you are not using "https://localhost" for the callback url.
3. This callback url should work: "https://127.0.0.1"

**Q: For "App Authorization" when you paste the url in the browser, you get "we are unable to complete your request**

This most likely is becuase of url encoding of the the redirect uri. Try to paste the url without url encoding like this: `&redirect_uri=https://127.0.0.1:8080`

**Q: Market data API is returning empty response**

Make surre to include the following header in your request:
* "Schwab-Client-CorrelId": "dummy"
* Ideally, you should put a GUID string for its value, but putting "dummy" should also work.

**Q: Market data API is returning binary response**

The response is compressed. You have to use proper library with proper option to uncompress the response. 
* Python - `requests` module does automatic uncompress whenever needed
* Curl command - Use `--compress` option to atuomatically uncompress the response if needed
 

# Communication Updates

**5/8**

Is your Schwab account enabled for trading with thinkorswim (tos)? If your account has not yet been enabled for tos, it will not have order entry or Account Access capabilities through the Trader API, which would cause any Place Order requests to fail. (Only Market Data requests would be available for accounts not enabled for tos.)

To see if your account still needs to be enabled for trading on thinkorswim, you would need to login online (Schwab.com), navigate to Trade > Trading Platforms, click 'Learn how to enable thinkorswim', and complete the agreement steps.
 
Schwab's enablement process happens overnight for most account types and will be ready in advance of market open. Once enabled, you should be able to send order requests through using the API.
 

**4/21**

The WebSocket based streaming API has not been released to production at this time, we are planning on releasing the streamer API in the near future. Documentation for the streaming API will also be posted to the Developer Portal as it becomes available.
 
Certain account types like Joint Tenant accounts, as well as any accounts that you are listed as an 'authorized user', are not currently supported by the Trader API, however; there is an overnight update scheduled to take place on 04/29/24 that should enable access to the API for a majority of these types of account, which should hopefully resolve this issue for you. However, please be sure to keep in mind that all dates mentioned are tentative and may still be subject to change. In this case it is unlikely that the update will be delayed, but there is always a possibility with these types of things.

**4/2**

 You DO NOT need to add the market data if you have an Ready to Use app.
 Once you create an app in the portal, it CAN NOT be deleted ever.

**3/28**

We will be releasing streaming API documentation soon as well, it most likely will be post the initial API release, I do not have an exact date when we will be uploading streaming API documentation.

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

