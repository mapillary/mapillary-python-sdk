---
sidebar position: 5
---


### mapillary.utils.format

This module deals with converting data to and from different file formats.


* Copyright: (c) 2021 Facebook


* License: MIT LICENSE


### mapillary.utils.format.decode_pixel_geometry(base64_string: str, normalized: bool = True, width: int = 4096, height: int = 4096)
Decodes the pixel geometry, and return the coordinates, which can be specified to be
normalized


* **Parameters**

    
    * **base64_string** (*str*) – The pixel geometry encoded as a vector tile


    * **normalized** (*bool*) – If normalization is required, defaults to True


    * **width** (*int*) – The width of the pixel geometry, defaults to 4096


    * **height** (*int*) – The height of the pixel geometry, defaults to 4096



* **Returns**

    A dictionary with coordinates as key, and value as the normalized list



* **Return type**

    list



### mapillary.utils.format.decode_pixel_geometry_in_geojson(geojson: Union[dict, mapillary.models.geojson.GeoJSON], normalized: bool = True, width: int = 4096, height: int = 4096)
Decodes all the pixel_geometry


* **Parameters**

    
    * **geojson** – The GeoJSON representation to be decoded


    * **normalized** (*bool*) – If normalization is required, defaults to True


    * **width** (*int*) – The width of the pixel geometry, defaults to 4096


    * **height** (*int*) – The height of the pixel geometry, defaults to 4096



### mapillary.utils.format.detection_features_to_geojson(feature_list: list)
Converts a preprocessed list (i.e, features from the detections of either images or
map_features from multiple segments) into a fully featured GeoJSON


* **Parameters**

    **feature_list** (*list*) – A list of processed features merged from different segments within a
    detection



* **Returns**

    GeoJSON formatted as expected in a detection format



* **Return type**

    dict


Example:

```
>>> # From
>>> [{'created_at': '2021-05-20T17:49:01+0000', 'geometry':
... 'GjUKBm1weS1vchIVEgIAABgDIg0JhiekKBoqAABKKQAPGgR0eXBlIgkKB3BvbHlnb24ogCB4AQ==',
... 'image': {'geometry': {'type': 'Point', 'coordinates': [-97.743279722222,
... 30.270651388889]}, 'id': '1933525276802129'}, 'value': 'regulatory--no-parking--g2',
... 'id': '1942105415944115'}, ... ]
>>> # To
>>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
... {'type': 'Point', 'coordinates': [-97.743279722222, 30.270651388889]}, 'properties': {
... 'image_id': '1933525276802129', 'created_at': '2021-05-20T17:49:01+0000',
... 'pixel_geometry':
... 'GjUKBm1weS1vchIVEgIAABgDIg0JhiekKBoqAABKKQAPGgR0eXBlIgkKB3BvbHlnb24ogCB4AQ==',
... 'value': 'regulatory--no-parking--g2', 'id': '1942105415944115' } }, ... ]}
```


### mapillary.utils.format.feature_to_geojson(json_data: dict)
Converts feature into a GeoJSON, returns output

From:

```
>>> {'geometry': {'type': 'Point', 'coordinates': [30.003755665554, 30.985948744314]},
... 'id':'506566177256016'}
```

To:

```
>>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type':
... 'Point','coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]}
```


* **Parameters**

    **json_data** (*dict*) – The feature as a JSON



* **Returns**

    The formatted GeoJSON



* **Return type**

    dict



### mapillary.utils.format.flatten_dictionary(data: Union[dict, collections.abc.MutableMapping], parent_key: str = '', sep: str = '_')
Flattens dictionaries

From:

```
>>> {'mpy-or': {'extent': 4096, 'version': 2, 'features': [{'geometry': {'type':
... 'Polygon', 'coordinates': [[[2402, 2776], [2408, 2776]]]}, 'properties': {}, 'id': 1,
... 'type': 3}]}}
```

To:

```
>>> {'mpy-or_extent': 4096, 'mpy-or_version': 2, 'mpy-or_features': [{'geometry':
... {'type':'Polygon', 'coordinates': [[[2402, 2776], [2408, 2776]]]}, 'properties':
... {}, 'id': 1,'type': 3}]}
```


* **Parameters**

    
    * **data** (*dict*) – The dictionary itself


    * **parent_key** (*str*) – The root key to start from


    * **sep** (*str*) – The separator



* **Returns**

    A flattened dictionary



* **Return type**

    dict



### mapillary.utils.format.flatten_geojson(geojson: dict)
Flattens a GeoJSON dictionary to a dictionary with only the relevant keys.
This is useful for writing to a CSV file.

Output Structure:

```
>>> {
...     "geometry": {
...         "type": "Point",
...         "coordinates": [71.45343, 12.523432]
...     },
...     "first_seen_at": "UNIX_TIMESTAMP",
...     "last_seen_at": "UNIX_TIMESTAMP",
...     "value": "regulatory--no-parking--g2",
...     "id": "FEATURE_ID",
...     "image_id": "IMAGE_ID"
... }
```


* **Parameters**

    **geojson** (*dict*) – The GeoJSON to flatten



* **Returns**

    A flattened GeoJSON



* **Return type**

    dict


Note,

    
    1. The geometry key is always present in the output


    2. The properties are flattened to the following keys:


            * “first_seen_at”   (optional)


            * “last_seen_at”    (optional)


            * “value”           (optional)


            * “id”              (required)


            * “image_id”        (optional)


            * etc.


    3. If the ‘geometry\` type is Point, two more properties will be added:


            * “longitude”


            * “latitude”

*TODO*: Further testing needed with different geometries, e.g., Polygon, etc.


### mapillary.utils.format.geojson_to_features_list(json_data: dict)
Converts a decoded output GeoJSON to a list of feature objects

The purpose of this formatting utility is to obtain a list of individual features for
decoded tiles that can be later extended to the output GeoJSON

From:

```
>>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
... {'type': 'Point','coordinates': [30.98594605922699, 30.003757307208872]},
... 'properties': {}}]}
```

To:

```
>>> [{'type': 'Feature', 'geometry': {'type': 'Point',
... 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}]
```


* **Parameters**

    **json_data** (*dict*) – The given json data



* **Returns**

    The feature list



* **Return type**

    list



### mapillary.utils.format.geojson_to_polygon(geojson: dict)
Converts a GeoJSON into a collection of only geometry coordinates for the purpose of
checking whether a given coordinate point exists within a shapely polygon

From:

```
>>> {
...     "type": "FeatureCollection",
...     "features": [
...         {
...             "geometry": {
...                 "coordinates": [
...                     -80.13069927692413,
...                     25.78523699486192
...                 ],
...                 "type": "Point"
...             },
...             "properties": {
...                 "first_seen_at": 1422984049000,
...                 "id": 481978503020355,
...                 "last_seen_at": 1422984049000,
...                 "value": "object--street-light"
...             },
...             "type": "Feature"
...         },
...         {
...             "geometry": {
...                 "coordinates": [
...                     -80.13210475444794,
...                     25.78362849816017
...                 ],
...                 "type": "Point"
...             },
...             "properties": {
...                 "first_seen_at": 1423228306666,
...                 "id": 252538103315239,
...                 "last_seen_at": 1423228306666,
...                 "value": "object--street-light"
...             },
...             "type": "Feature"
...         },
...         ...
...     ]
... }
```

To:

```
>>> {
... "type": "FeatureCollection",
... "features": [
...         {
...             "type": "Feature",
...             "properties": {},
...             "geometry": {
...                 "type": "Polygon",
...                 "coordinates": [
...                     [
...                         [
...                             7.2564697265625,
...                             43.69716905314008
...                         ],
...                         [
...                             7.27020263671875,
...                             43.69419030566581
...                         ],
...                         ...
...                     ]
...                 ]
...             }
...         }
...     ]
... }
```


* **Parameters**

    **geojson** (*dict*) – The input GeoJSON



* **Returns**

    A geojson of the format mentioned under ‘To’



* **Return type**

    dict



### mapillary.utils.format.join_geojson_with_keys(geojson_src: dict, geojson_src_key: str, geojson_dest: dict, geojson_dest_key: str)
Combines two GeoJSONS based on the similarity of their specified keys, similar to
the SQL join functionality


* **Parameters**

    
    * **geojson_src** (*dict*) – The starting GeoJSO source


    * **geojson_src_key** (*str*) – The key in properties specified for the GeoJSON source


    * **geojson_dest** (*dict*) – The GeoJSON to merge into


    * **geojson_dest_key** (*dict*) – The key in properties specified for the GeoJSON to merge into



* **Returns**

    The merged GeoJSON



* **Return type**

    dict


Usage:

```
>>> join_geojson_with_keys(
...     geojson_src=geojson_src,
...     geojson_src_key='id',
...     geojson_dest=geojson_dest,
...     geojson_dest_key='id'
... )
```


### mapillary.utils.format.merged_features_list_to_geojson(features_list: list)
Converts a processed features list (i.e. a features list with all the needed features merged
from multiple tiles) into a fully-featured GeoJSON

From:

```
>>> [{'type': 'Feature', 'geometry': {'type': 'Point',
... 'coordinates': [30.98594605922699, 30.003757307208872]}, 'properties': {}}, ...]
```

To:

```
>>> {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry':
... {'type': 'Point','coordinates': [30.98594605922699, 30.003757307208872]},
... 'properties': {}}, ...]}
```


* **Parameters**

    **features_list** (*list*) – a list of processed features merged from different tiles within a bbox



* **Returns**

    GeoJSON string formatted with all the extra commas removed.



* **Return type**

    str



### mapillary.utils.format.normalize_list(coordinates: list, width: int = 4096, height: int = 4096)
Normalizes a list of coordinates with the respective width and the height

From:

```
>>> [[[2402, 2776], [2408, 2776]]]
```

To:

```
>>> normalize_list(coordinates)
... # [[[0.58642578125, 0.677734375], [0.587890625, 0.677734375]]]
```


* **Parameters**

    
    * **coordinates** (*list*) – The coordinate list to normalize


    * **width** (*int*) – The width of the coordinates to normalize with, defaults to 4096


    * **height** (*int*) – The height of the coordinates to normalize with, defaults to 4096



* **Returns**

    The normalized list



* **Return type**

    list

