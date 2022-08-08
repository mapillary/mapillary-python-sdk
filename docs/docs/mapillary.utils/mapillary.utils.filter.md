---
sidebar position: 4
---


### mapillary.utils.filter

This module contains the filter utilies for high level filtering logic


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### mapillary.utils.filter.by_look_at_feature(image: dict, look_at_feature: Feature)
Filter through the given image features and return only features with the look_at_feature


* **Parameters**

    
    * **image** (*dict*) – The feature dictionary


    * **look_at_feature** (*A WGS84 GIS feature**, **TurfPy*) – Feature description



* **Returns**

    Whether the given feature is looking at the look_at_features



* **Return type**

    bool



### mapillary.utils.filter.compass_angle(data: list, angles: tuple = (0.0, 360.0))
Filter out images that do not lie within compass angle range


* **Parameters**

    
    * **data** (*list*) – The data to be filtered


    * **angles** – The compass angle range to filter through



* **Returns**

    A feature list



* **Return type**

    list



### mapillary.utils.filter.existed_at(data: list, existed_at: str)
Whether the first_seen_at properly existed after a specified time period


* **Parameters**

    
    * **data** (*list*) – The feature list


    * **existed_at** (*str*) – The UNIX timestamp



* **Returns**

    The feature list



* **Return type**

    list



### mapillary.utils.filter.existed_before(data: list, existed_before: str)
Whether the first_seen_at properly existed before a specified time period


* **Parameters**

    
    * **data** (*list*) – The feature list


    * **existed_before** (*str*) – The UNIX timestamp



* **Returns**

    A feature list



* **Return type**

    list



### mapillary.utils.filter.features_in_bounding_box(data: list, bbox: dict)
Filter for extracting features only in a bounding box


* **Parameters**

    
    * **data** (*list*) – the features list to be checked


    * **bbox** (*dict*) – Bounding box coordinates

    Example::

        ```python
        >>> {
        ...     'west': 'BOUNDARY_FROM_WEST',
        ...     'south': 'BOUNDARY_FROM_SOUTH',
        ...     'east': 'BOUNDARY_FROM_EAST',
        ...     'north': 'BOUNDARY_FROM_NORTH'
        ... }
        ```




* **Returns**

    Features that only exist within the bounding box selected for the given features list
    provided in the BBox functon



* **Return type**

    list



### mapillary.utils.filter.filter_values(data: list, values: list, property: str = 'value')
Filter the features based on the existence of a specified value
in one of the property.

*TODO*: Need documentation that lists the ‘values’, specifically, it refers to ‘value’
*TODO*: under ‘Detection’, and ‘Map feature’, related to issue #65


* **Parameters**

    
    * **data** (*dict*) – The data to be filtered


    * **values** (*list*) – A list of values to filter by


    * **property** (*str*) – The specific parameter to look into



* **Returns**

    A feature list



* **Return type**

    dict



### mapillary.utils.filter.haversine_dist(data: dict, radius: float, coords: list, unit: str = 'm')
Returns features that are only in the radius specified using the Haversine distance, from
the haversine package


* **Parameters**

    
    * **data** (*dict*) – The data to be filtered


    * **radius** (*float*) – Radius for coordinates to fall into


    * **coords** (*list*) – The input coordinates (long, lat)


    * **unit** (*str*) – Either ‘ft’, ‘km’, ‘m’, ‘mi’, ‘nmi’, see here [https://pypi.org/project/haversine/](https://pypi.org/project/haversine/)



* **Returns**

    A feature list



* **Return type**

    list



### mapillary.utils.filter.hits_by_look_at(data: list, at: dict)
Whether the given data have any feature that look at the at coordinates


* **Parameters**

    
    * **data** (*list*) – List of features with an Image entity


    * **at** (*dict*) – The lng and lat coordinates

    Example:

    ```
    >>> {
    ...     'lng': 'longitude',
    ...     'lat': 'latitude'
    ... }
    ```




* **Returns**

    Filtered results of features only looking at at



* **Return type**

    list



### mapillary.utils.filter.image_type(data: list, image_type: str)
The parameter might be ‘all’ (both is_pano == true and false), ‘pano’ (is_pano == true only),
or ‘flat’ (is_pano == false only)


* **Parameters**

    
    * **data** (*list*) – The data to be filtered


    * **image_type** (*str*) – Either ‘pano’ (True), ‘flat’ (False), or ‘all’ (None)



* **Returns**

    A feature list



* **Return type**

    list



### mapillary.utils.filter.in_shape(data: list, boundary)
Whether the given feature list lies within the shape


* **Parameters**

    
    * **data** (*list*) – A feature list to be filtered


    * **boundary** – Shapely helper for determining existence of point within a boundary



* **Returns**

    A feature list



* **Return type**

    list



### mapillary.utils.filter.is_looking_at(image_feature: Feature, look_at_feature: Feature)
Return whether the image_feature is looking at the look_at_feature


* **Parameters**

    
    * **image_feature** (*dict*) – The feature set of the image


    * **look_at_feature** (*dict*) – The feature that is being looked at



* **Returns**

    Whether the diff is greater than 310, or less than 50



* **Return type**

    bool



### mapillary.utils.filter.max_captured_at(data: list, max_timestamp: str)
Selects only the feature items that are less
than the max_timestamp


* **Parameters**

    
    * **data** (*list*) – The feature list


    * **max_timestamp** (*str*) – The UNIX timestamp as the max time



* **Returns**

    Filtered feature list



* **Return type**

    list


Usage:

```
>>> max_captured_at([{'type': 'Feature', 'geometry':
... {'type': 'Point', 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties':
... { ... }, ...}], '2020-05-23')
```


### mapillary.utils.filter.min_captured_at(data: list, min_timestamp: str)
Selects only the feature items that are less
than the min_timestamp


* **Parameters**

    
    * **data** (*list*) – The feature list


    * **min_timestamp** (*str*) – The UNIX timestamp as the max time



* **Returns**

    Filtered feature list



* **Return type**

    list


Usage:

```
>>> max_captured_at([{'type': 'Feature', 'geometry':
... {'type': 'Point', 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties':
... { ... }, ...}], '2020-05-23')
```


### mapillary.utils.filter.organization_id(data: list, organization_ids: list)
Select only features that contain the specific organization_id


* **Parameters**

    
    * **data** (*dict*) – The data to be filtered


    * **organization_ids** (*list*) – The oragnization id(s) to filter through



* **Returns**

    A feature list



* **Return type**

    dict



### mapillary.utils.filter.pipeline(data: dict, components: list)
A pipeline component that helps with making filtering easier. It provides
access to different filtering mechanism by simplying letting users
pass in what filter they want to apply, and the arguments for that filter


* **Parameters**

    
    * **data** (*dict*) – The GeoJSON to be filtered


    * **components** (*list*) – The list of filters to apply



* **Returns**

    The filtered feature list



* **Return type**

    list


Usage:

```
>>> # assume variables 'data', 'kwargs'
>>> pipeline(
...     data=data,
...     components=[
...         {"filter": "image_type", "tile": kwargs["image_type"]}
...         if "image_type" in kwargs
...         else {},
...         {"filter": "organization_id", "organization_ids": kwargs["org_id"]}
...         if "org_id" in kwargs
...         else {},
...         {
...             "filter": "haversine_dist",
...             "radius": kwargs["radius"],
...             "coords": [longitude, latitude],
...         }
...         if "radius" in kwargs
...         else 1000
...     ]
... )
```


### mapillary.utils.filter.pipeline_component(func, data: list, exception_message: str, args: list)
A pipeline component which is respnonsible for sending functional arguments over
to the selected target function - throwing a warning in case of an exception


* **Parameters**

    
    * **func** (*function*) – The filter to apply


    * **data** (*list*) – The list of features to filter


    * **exception_message** (*str*) – The exception message to print


    * **args** (*list*) – Arguments



* **Returns**

    The filtered feature list



* **Return type**

    list


Usage:

```
>>> # internally used in mapillary.utils.pipeline
```


### mapillary.utils.filter.sequence_id(data: list, ids: list)
Filter out images that do not have the sequence_id in the list of ids


* **Parameters**

    
    * **data** (*list*) – The data to be filtered


    * **ids** (*list*) – The sequence id(s) to filter through



* **Returns**

    A feature list



* **Return type**

    list

