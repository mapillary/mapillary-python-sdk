---
sidebar position: 3
---


### mapillary.models.exceptions

This module contains the set of Mapillary Exceptions used internally.

For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### exception mapillary.models.exceptions.AuthError(message: str)
Bases: `MapillaryException`

Raised when a function is called without having the access token set in
set_access_token to access Mapillary’s API, primarily used in mapillary.set_access_token


* **Variables**

    **message** – The error message returned



### exception mapillary.models.exceptions.InvalidBBoxError(message: str)
Bases: `MapillaryException`

Raised when an invalid coordinates for bounding box are entered
to access Mapillary’s API.


* **Variables**

    **message** – The error message returned



### exception mapillary.models.exceptions.InvalidFieldError(endpoint: str, field: list)
Bases: `MapillaryException`

Raised when an API endpoint is passed invalid field elements


* **Variables**

    
    * **endpoint** – The API endpoint that was targeted


    * **field** – The invalid field that was passed



### exception mapillary.models.exceptions.InvalidImageKeyError(image_id: Union[int, str])
Bases: `MapillaryException`

Raised when trying to retrieve an image thumbnail with an invalid image ID/key.
Primarily used with mapillary.image_thumbnail


* **Variables**

    **image_id** – Image ID/key entered by the user



* **Parameters**

    **image_id** – int



### exception mapillary.models.exceptions.InvalidImageResolutionError(resolution: int)
Bases: `MapillaryException`

Raised when trying to retrieve an image thumbnail with an invalid resolution/size.

Primarily used with mapillary.image_thumbnail


* **Variables**

    **resolution** – Image size entered by the user



### exception mapillary.models.exceptions.InvalidKwargError(func: str, key: str, value: str, options: list)
Bases: `MapillaryException`

Raised when a function is called with the invalid keyword argument(s) that do not belong to the
requested API end call


* **Variables**

    
    * **func** – The function that was called


    * **key** – The key that was passed


    * **value** – The value along with that key


    * **options** – List of possible keys that can be passed



### exception mapillary.models.exceptions.InvalidOptionError(param: str, value: any, options: list)
Bases: `MapillaryException`

Out of bound zoom error


* **Variables**

    
    * **param** – The invalid param passed


    * **value** – The invalid value passed


    * **options** – The possible list of zoom values



### exception mapillary.models.exceptions.InvalidTokenError(message: str, error_type: str, code: str, fbtrace_id: str)
Bases: `MapillaryException`

Raised when an invalid token is given
to access Mapillary’s API, primarily used in mapillary.set_access_token


* **Variables**

    
    * **message** – The error message returned


    * **error_type** – The type of error that occurred


    * **code** – The error code returned, most likely 190, “Access token has expired”.
    See [https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/](https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/)
    for more information


    * **fbtrace_id** – A unique ID to track the issue/exception



### exception mapillary.models.exceptions.LiteralEnforcementException(\*args: object)
Bases: `MapillaryException`

Raised when literals passed do not correspond to options


#### static enforce_literal(function: any)

### exception mapillary.models.exceptions.MapillaryException()
Bases: `Exception`

Base class for exceptions in this module
