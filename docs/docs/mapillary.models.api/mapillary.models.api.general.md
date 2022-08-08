---
sidebar position: 3
---


### mapillary.models.api.entities

This module contains the Adapter design for the Entities API of Mapillary API v4.

For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/).


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### class mapillary.models.api.general.GeneralAdapter(\*args: object)
Bases: `object`

General adaptor for using the API calls defined for the general module
(mapillary.config.api.general)

The GeneralAdaptor provides functions for getting preprocessed data from the API, through the
API calls mentioned in the previously mentioned config.

It performs parsing, property handling, easier logic for extracing information, focusing on
adding a layer of abstraction by removing details of using mercantile, ast, et al, to
focus on the inputs and outputs of functions

Usage:

```
>>> import mapillary
```


#### fetch_computed_image_tiles(zoom: int, longitude: float, latitude: float, layer: Literal['overview', 'sequence', 'image', 'map_feature', 'traffic_sign'] = 'image')
Get the image type for a given image.


* **Parameters**

    
    * **zoom** (*int*) – The zoom to get the image type for.


    * **longitude** (*float*) – The longitude of the image.


    * **latitude** (*float*) – The latitude of the image.



* **Returns**

    A dictionary containing the image type for the image.



* **Return type**

    dict



#### fetch_image_tiles(zoom: int, longitude: float, latitude: float, layer: Literal['overview', 'sequence', 'image', 'map_feature', 'traffic_sign'] = 'image')
Get the tiles for a given image.


* **Parameters**

    
    * **zoom** (*int*) – Zoom level of the image.


    * **longitude** (*float*) – Longitude of the image


    * **latitude** (*float*) – Latitude of the image



* **Returns**

    A dictionary containing the tiles for the image.



* **Return type**

    dict



#### fetch_map_features_tiles(zoom: int, longitude: float, latitude: float, layer: Literal['overview', 'sequence', 'image', 'map_feature', 'traffic_sign'] = 'image')
Get the map features for a given coordinate set


* **Parameters**

    
    * **zoom** (*int*) – The zoom value to get the map features for


    * **longitude** (*float*) – The longitude of the image


    * **latitude** (*float*) – The latitude of the image



* **Returns**

    A dictionary containing the map features for the image.



* **Return type**

    dict



#### fetch_map_features_traffic_tiles(zoom: int, longitude: float, latitude: float, layer: str)
Get the map feature traffic for a given coordinate set


* **Parameters**

    
    * **zoom** (*int*) – The zoom value to get the map features for


    * **longitude** (*float*) – The longitude of the image


    * **latitude** (*float*) – The latitude of the image



* **Returns**

    A dictionary containing the map features for the image.



* **Return type**

    dict

