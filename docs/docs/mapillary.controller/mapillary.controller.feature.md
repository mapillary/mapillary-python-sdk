---
sidebar position: 3
---


### mapillary.controllers.feature

This module implements the feature extraction business logic functionalities of the Mapillary
Python SDK.

For more information, please check out [https://www.mapillary.com/developer/api-documentation/](https://www.mapillary.com/developer/api-documentation/)


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### mapillary.controller.feature.get_feature_from_key_controller(key: int, fields: list)
A controller for getting properties of a certain image given the image key and
the list of fields/properties to be returned


* **Parameters**

    
    * **key** (*int*) – The image key


    * **fields** (*list*) – List of possible fields



* **Returns**

    The requested feature properties in GeoJSON format



* **Return type**

    str



### mapillary.controller.feature.get_map_features_in_bbox_controller(bbox: dict, filter_values: list, filters: dict, layer: str = 'points')
For extracting either map feature points or traffic signs within a bounding box


* **Parameters**

    
    * **bbox** (*dict*) – Bounding box coordinates as argument


    * **layer** (*str*) – ‘points’ or ‘traffic_signs’


    * **filter_values** (*list*) – a list of filter values supported by the API.


    * **filters** (*dict*) – Chronological filters



* **Returns**

    GeoJSON



* **Return type**

    str

