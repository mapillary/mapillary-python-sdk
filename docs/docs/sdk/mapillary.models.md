---
sidebar_position: 6
---

# mapillary.models package
 
 ## Subpackages
 
 
 * mapillary.models.api package
 
 
     * Submodules
 
 
     * mapillary.models.api.entities module
 
 
         * mapillary.models.api.entities
 
 
     * mapillary.models.api.vector_tiles module
 
 
         * mapillary.models.api.vector_tiles
 
 
     * Module contents
 
 
         * mapillary.models.api.__init__
 
 
 ## Submodules
 
 ## mapillary.models.client module
 
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
 
 
 ## mapillary.models.exceptions module
 
 ### mapillary.models.exceptions
 
 This module contains the set of Mapillary Exceptions used internally.
 
 For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### exception mapillary.models.exceptions.AuthError(message: str)
 Bases: `mapillary.models.exceptions.MapillaryException`
 
 Raised when a function is called without having the access token set in
 set_access_token to access Mapillary’s API, primarily used in mapillary.set_access_token
 
 
 * **Variables**
 
     **message** – The error message returned
 
 
 
 ### exception mapillary.models.exceptions.InvalidFieldError(endpoint: str, field: list)
 Bases: `mapillary.models.exceptions.MapillaryException`
 
 Raised when an API endpoint is passed invalid field elements
 
 
 * **Variables**
 
     
     * **endpoint** – The API endpoint that was targeted
 
 
     * **field** – The invalid field that was passed
 
 
 
 ### exception mapillary.models.exceptions.InvalidImageKeyError(image_id: Union[int, str])
 Bases: `mapillary.models.exceptions.MapillaryException`
 
 Raised when trying to retrieve an image thumbnail with an invalid image ID/key.
 Primarily used with mapillary.image_thumbnail
 
 
 * **Variables**
 
     **image_id** – Image ID/key entered by the user
 
 
 
 * **Parameters**
 
     **image_id** – int
 
 
 
 ### exception mapillary.models.exceptions.InvalidImageResolutionError(resolution: int)
 Bases: `mapillary.models.exceptions.MapillaryException`
 
 Raised when trying to retrieve an image thumbnail with an invalid resolution/size.
 
 Primarily used with mapillary.image_thumbnail
 
 
 * **Variables**
 
     **resolution** – Image size entered by the user
 
 
 
 ### exception mapillary.models.exceptions.InvalidKwargError(func: str, key: str, value: str, options: list)
 Bases: `mapillary.models.exceptions.MapillaryException`
 
 Raised when a function is called with the invalid keyword argument(s) that do not belong to the
 requested API end call
 
 
 * **Variables**
 
     
     * **func** – The function that was called
 
 
     * **key** – The key that was passed
 
 
     * **value** – The value along with that key
 
 
     * **options** – List of possible keys that can be passed
 
 
 
 ### exception mapillary.models.exceptions.InvalidOptionError(param: str, value: any, options: list)
 Bases: `mapillary.models.exceptions.MapillaryException`
 
 Out of bound zoom error
 
 
 * **Variables**
 
     
     * **param** – The invalid param passed
 
 
     * **value** – The invalid value passed
 
 
     * **options** – The possible list of zoom values
 
 
 
 ### exception mapillary.models.exceptions.InvalidTokenError(message: str, error_type: str, code: str, fbtrace_id: str)
 Bases: `mapillary.models.exceptions.MapillaryException`
 
 Raised when an invalid token is given
 to access Mapillary’s API, primarily used in mapillary.set_access_token
 
 
 * **Variables**
 
     
     * **message** – The error message returned
 
 
     * **error_type** – The type of error that occurred
 
 
     * **code** – The error code returned, most likely 190, “Access token has expired”.
     See [https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/](https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/)
     for more information
 
 
     * **fbtrace_id** – A unique ID to track the issue/exception
 
 
 
 ### exception mapillary.models.exceptions.MapillaryException()
 Bases: `Exception`
 
 Base class for exceptions in this module
 
 ## mapillary.models.geojson module
 
 ### mapillary.models.geojson
 
 This module contains the class implementation for the geojson
 
 For more information about the API, please check out
 [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
 
 
 ### class mapillary.models.geojson.Feature(feature: dict)
 Bases: `object`
 
 Representation for a feature in a feature list
 
 
 * **Parameters**
 
     **feature** (*dict*) – The GeoJSON as the input
 
 
 
 * **Raises**
 
     **InvalidOptionError** – Raised when the geojson passed is the invalid type - not a dict
 
 
 
 * **Returns**
 
     A class representation of the model
 
 
 
 * **Return type**
 
     <class ‘mapillary.models.geojson.Feature’>
 
 
 
 #### to_dict()
 Return the dictionary representation of the Feature
 
 
 ### class mapillary.models.geojson.GeoJSON(geojson: dict)
 Bases: `object`
 
 Representation for a geojson
 
 
 * **Parameters**
 
     **geojson** (*dict*) – The GeoJSON as the input
 
 
 
 * **Raises**
 
     **InvalidOptionError** – Raised when the geojson passed is the invalid type - not a dict
 
 
 
 * **Returns**
 
     A class representation of the model
 
 
 
 * **Return type**
 
     <class ‘mapillary.models.geojson.GeoJSON’>
 
 
 Usage:
 
 ```
 >>> import mapillary as mly
 >>> from models.geojson import GeoJSON
 >>> mly.interface.set_access_token('MLY|XXX')
 >>> data = mly.interface.get_image_close_to(longitude=31, latitude=31)
 >>> geojson = GeoJSON(geojson=data)
 >>> type(geojson)
 ... <class 'mapillary.models.geojson.GeoJSON'>
 >>> type(geojson.type)
 ... <class 'str'>
 >>> type(geojson.features)
 ... <class 'list'>
 >>> type(geojson.features[0])
 ... <class 'mapillary.models.geojson.Feature'>
 >>> type(geojson.features[0].type)
 ... <class 'str'>
 >>> type(geojson.features[0].geometry)
 ... <class 'mapillary.models.geojson.Geometry'>
 >>> type(geojson.features[0].geometry.type)
 ... <class 'str'>
 >>> type(geojson.features[0].geometry.coordinates)
 ... <class 'list'>
 >>> type(geojson.features[0].properties)
 ... <class 'mapillary.models.geojson.Properties'>
 >>> type(geojson.features[0].properties.captured_at)
 ... <class 'int'>
 >>> type(geojson.features[0].properties.is_pano)
 ... <class 'str'>
 ```
 
 
 #### append_feature(feature_inputs: dict)
 Given a feature dictionary, append it to the GeoJSON object
 
 
 * **Parameters**
 
     **feature_inputs** (*dict*) – A feature as dict
 
 
 
 * **Returns**
 
     None
 
 
 
 #### append_features(features: list)
 Given a feature list, append it to the GeoJSON object
 
 
 * **Parameters**
 
     **features** (*list*) – A feature list
 
 
 
 * **Returns**
 
     None
 
 
 
 #### encode()
 Serializes the GeoJSON object
 
 
 * **Returns**
 
     Serialized GeoJSON
 
 
 
 #### to_dict()
 Return the dict format representation of the GeoJSON
 
 
 ### class mapillary.models.geojson.Geometry(geometry: dict)
 Bases: `object`
 
 Representation for the geometry in a GeoJSON
 
 
 * **Parameters**
 
     **geometry** (*dict*) – The geometry as the input
 
 
 
 * **Raises**
 
     **InvalidOptionError** – Raised when the geometry passed is the invalid type - not a dict
 
 
 
 * **Returns**
 
     A class representation of the model
 
 
 
 * **Return type**
 
     <class ‘mapillary.models.geojson.Geometry’>
 
 
 
 #### to_dict()
 Return dictionary representation of the geometry
 
 
 ### class mapillary.models.geojson.Properties(\*properties, \*\*kwargs)
 Bases: `object`
 
 Representation for the properties in a GeoJSON
 
 
 * **Parameters**
 
     **properties** (*dict*) – The properties as the input
 
 
 
 * **Raises**
 
     **InvalidOptionError** – Raised when the geojson passed is the invalid type - not a dict
 
 
 
 * **Returns**
 
     A class representation of the model
 
 
 
 * **Return type**
 
     <class ‘mapillary.models.geojson.Properties’>
 
 
 
 #### to_dict()
 Return the dictionary representation of the Properties
 
 ## Module contents
 
 ### mapillary.models.__init__
 
 This package contains the class representations of logic within the Mapillary Python SDK.
 
 
 * Copyright: (c) 2021 Facebook
 
 
 * License: MIT LICENSE
