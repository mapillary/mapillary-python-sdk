"""
mapillary.config.api

This module contains the APIv4 configuration
and URL arguments. Created to help in ease of
use of the APIv4

# SOME NOTES FROM THE API,

## Over Authentication

1. All requests against https://graph.mapillary.com
must be authorized. They require a client or user
access tokens. Tokens can be sent in two ways
    1. Using ?access_token=XXX query parameters. This
    is a preferred method for interacting with vector
    tiles. Using this method is STRONGLY discouraged
    for sending user access tokens
    2. using a header such as Authorization: OAuth XXX,
    where XXX is the token obtained either through the
    OAuth flow that your application implements or a
    client token from https://mapillary.com/dashboard/developers
    This method works for the Entity API

REFERENCE,

1. https://www.mapillary.com/developer/api-documentation/
2. https://blog.mapillary.com/update/2021/06/23/getting-started-with-\
the-new-mapillary-api-v4.html
"""
