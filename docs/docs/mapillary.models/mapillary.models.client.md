---
sidebar position: 2
---


### mapillary.models.client

This module contains aims to serve as a generalization for all API requests within the Mapillary
Python SDK.

#### Over Authentication


1. All requests against [https://graph.mapillary.com](https://graph.mapillary.com) must be authorized. They require a client or

    user access tokens. Tokens can be sent in two ways,


        1. Using ?access_token=XXX query parameters. This is a preferred method for interacting with

        vector tiles. Using this method is STRONGLY discouraged for sending user access tokens


        2. Using a header such as Authorization: OAuth XXX, where XXX is the token obtained either

        through the OAuth flow that your application implements or a client token from
        [https://mapillary.com/dashboard/developers](https://mapillary.com/dashboard/developers).

For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### class mapillary.models.client.Client()
Bases: `object`

Client setup for API communication.

All requests for the Mapillary API v4 should go through this class

Usage:

```
>>> client = Client(access_token='MLY|XXX')
>>> # for entities endpoints
>>> client.get(endpoint='endpoint specific path', entity=True, params={
...     'fields': ['id', 'value']
... })
>>> # for tiles endpoint
>>> client.get(endpoint='endpoint specific path', entity=False)
```


#### get(url: Optional[str] = None, params: Optional[dict] = None)
Make GET requests to both mapillary main endpoints


* **Parameters**

    
    * **url** (*str*) – The specific path of the request URL


    * **params** (*dict*) – Query parameters to be attached to the URL (Dict)



#### static get_token()
Gets the access token


* **Returns**

    The access token



#### static set_token(access_token: str)
Sets the access token


* **Parameters**

    **access_token** – The access token to be set

